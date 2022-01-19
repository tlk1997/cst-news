package com.example.demo.pojo;

public class News {
    private int idx;
    private String title;
    private int time;
    private String url;

    public News(){}

    public News(int idx , String title, int time , String url){
        this.idx = idx;
        this.title = title;
        this.time = time;
        this.url = url;
    }

    public void setId(int idx) {
        this.idx = idx;
    }

    public void setTime(int time) {
        this.time = time;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public int getId() {
        return idx;
    }

    public int getTime() {
        return time;
    }

    public String getTitle() {
        return title;
    }

    public String getUrl() {
        return url;
    }
    @Override
    public String toString(){
        return idx + " " + title + " " + time + " " + url;
    }
}
