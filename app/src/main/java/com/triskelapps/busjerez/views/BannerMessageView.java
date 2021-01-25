package com.triskelapps.busjerez.views;

import android.content.Context;
import android.content.Intent;
import android.graphics.Color;
import android.net.SSLCertificateSocketFactory;
import android.net.Uri;
import android.text.TextUtils;
import android.util.AttributeSet;
import android.util.Log;
import android.util.Patterns;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.FrameLayout;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;
import com.google.android.gms.security.ProviderInstaller;
import com.triskelapps.busjerez.databinding.ViewBannerMessageBinding;
import com.triskelapps.busjerez.util.CountlyUtil;

import org.json.JSONException;
import org.json.JSONObject;


public class BannerMessageView extends FrameLayout implements View.OnClickListener {

    private static final String TAG = "UpdateAppView";

    public static final String URL_BANNER_MESSAGE_FILE = "https://triskelapps.es/apps/autobuses-jerez/banner_message.json";
    private String link;
    private ViewBannerMessageBinding binding;

    public BannerMessageView(Context context) {
        super(context);
        init();
    }


    public BannerMessageView(Context context, AttributeSet attrs) {
        super(context, attrs);
        init();
    }

    public BannerMessageView(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
        init();
    }

    private void init() {
        binding = ViewBannerMessageBinding.inflate(LayoutInflater.from(getContext()));

        addView(binding.getRoot());

        setVisibility(GONE);

        checkMessage();
    }

    private void checkMessage() {

        RequestQueue queue = Volley.newRequestQueue(getContext());

        JsonObjectRequest jsonObjectRequest = new JsonObjectRequest
                (Request.Method.GET, URL_BANNER_MESSAGE_FILE, null,
                        response -> processResponseJson(response),
                        error -> error.printStackTrace());


        jsonObjectRequest.setShouldCache(false);

        queue.add(jsonObjectRequest);

    }

    private void processResponseJson(JSONObject response) {

        try {
            boolean active = response.getBoolean("active");
            if (active) {

                String message = response.getString("message");
                String link = response.getString("link");
                String color = response.getString("color");
                String textColor = response.getString("text_color");

                if (!TextUtils.isEmpty(message)) {
                    binding.tvBannerMessage.setText(message);
                    setVisibility(VISIBLE);
                }

                if (!TextUtils.isEmpty(link) && Patterns.WEB_URL.matcher(link).matches()) {
                    this.link = link;
                    setOnClickListener(this);
                }

                try {
                    if (!TextUtils.isEmpty(color)) {
                        binding.getRoot().setBackgroundColor(Color.parseColor(color));
                    }

                    if (!TextUtils.isEmpty(textColor)) {
                        binding.tvBannerMessage.setTextColor(Color.parseColor(textColor));
                    }
                } catch (IllegalArgumentException e) {
                    Log.e(TAG, "processResponseJson: color cannot be parsed", e);
                }

            }
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }


    @Override
    public void onClick(View v) {

        if (link != null) {
            Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(link));
            if (intent.resolveActivity(getContext().getPackageManager()) != null) {
                getContext().startActivity(intent);
                CountlyUtil.bannerMessageClick(link);
            }
        }

    }


}
