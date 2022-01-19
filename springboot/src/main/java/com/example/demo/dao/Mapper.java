package com.example.demo.dao;

import com.example.demo.pojo.News;

import java.util.List;
import java.util.Map;

public interface Mapper {
    List<News> getNewsList(Map<String,Integer> map);
}
