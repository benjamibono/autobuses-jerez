package com.triskelapps.interactor;

import android.content.Context;
import android.database.Observable;
import android.util.Log;

import androidx.annotation.NonNull;
import androidx.work.impl.Schedulers;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.android.gms.tasks.Tasks;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.Query;
import com.google.firebase.firestore.QueryDocumentSnapshot;
import com.triskelapps.App;
import com.triskelapps.CityData;
import com.triskelapps.base.BaseInteractor;
import com.triskelapps.base.BaseView;
import com.triskelapps.model.News;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Callable;


/**
 * Created by julio on 8/10/17.
 */

public class NewsInteractor extends BaseInteractor {


    private static final String COLLECTION_NEWS = "news";

    public NewsInteractor(Context context, BaseView baseView) {
        super(context, baseView);
    }

    public void parseLinkDetails(final String link, CallbackGetEntity<News> callback) {

        Tasks.call((Callable<News>) () -> {

            News news = new News();

            Document doc = Jsoup.connect(link).get();

            Elements metaOgTitle = doc.select("meta[property=og:title]");
            if (metaOgTitle != null) {
                news.setTitle(metaOgTitle.attr("content"));
            } else {
                news.setTitle(doc.title());
            }

            Elements metaOgDescription = doc.select("meta[property=og:description]");
            if (metaOgDescription != null) {
                news.setSubtitle(metaOgDescription.attr("content"));
            }

            Elements metaOgSiteName = doc.select("meta[property=og:site_name]");
            if (metaOgSiteName != null) {
                news.setMedia(metaOgSiteName.attr("content"));
            }

            Elements metaOgImage = doc.select("meta[property=og:image]");
            if (metaOgImage != null) {
                news.setImage(metaOgImage.attr("content"));
            }

            Elements metaOgUrl = doc.select("meta[property=og:url]");
            if (metaOgUrl != null) {
                news.setUrl(metaOgUrl.attr("content"));
            } else {
                news.setUrl(link);
            }

            Elements metaOgDate = doc.select("meta[property=article:published_time]");
            if (metaOgDate != null && !metaOgDate.isEmpty()) {
                news.setDate(metaOgDate.attr("content").substring(0, 10));
            }


            return news;

        })
                .addOnCompleteListener(task -> {

                    if (task.isSuccessful()) {
                        callback.onEntityReceived(task.getResult());
                    } else {
                        callback.onError(task.getException().getMessage());
                    }
                });

    }

    public void getNews(final CallbackGetList<News> callback) {

        if (!isConnected()) {
            return;
        }

        final List<News> newsList = new ArrayList<>();

        FirebaseFirestore db = FirebaseFirestore.getInstance();

        db.collection(COLLECTION_NEWS)
                .orderBy(News.FIELD_DATE, Query.Direction.DESCENDING)
                .get()
                .addOnCompleteListener(task -> {

                    baseView.hideProgressDialog();

                    if (task.isSuccessful()) {
                        for (QueryDocumentSnapshot document : task.getResult()) {
                            News news = document.toObject(News.class);
                            newsList.add(news);
                            Log.d(TAG, document.getId() + " => " + document.getData());
                        }
                        callback.onListReceived(newsList);
                    } else {
                        Log.w(TAG, "Error getting documents.", task.getException());
                        callback.onError("Error getting documents." + task.getException().getMessage());
                    }

                });
    }

    public void sendNews(final News news, final CallbackPost callback) {

        if (!isConnected()) {
            return;
        }

        FirebaseFirestore db = FirebaseFirestore.getInstance();
        db.collection(COLLECTION_NEWS)
                .add(news)
                .addOnCompleteListener(task -> {

                    baseView.hideProgressDialog();

                    if (task.isSuccessful()) {
                        task.getResult().getId();
                        callback.onSuccess(null);
                    } else {
                        callback.onError(task.getException().getMessage());
                    }
                });

    }


}