package com.example.demo.controller;

import com.example.demo.dao.Mapper;
import com.example.demo.pojo.News;
import com.example.demo.utils.MybatisUtils;
import org.apache.ibatis.session.SqlSession;
import org.springframework.web.bind.annotation.*;

import java.util.*;

@CrossOrigin
@RestController
@RequestMapping("/get")
public class demoController {
    @GetMapping("/{start}")
    public List view(@PathVariable("start") int start){
        SqlSession sqlSession = MybatisUtils.getSqlSession();
        Mapper mapper = sqlSession.getMapper(Mapper.class);
        Map<String,Integer> map = new HashMap<>();
        map.put("startIndex" , start * 20);
        map.put("pageSize" , 20);
        List<News> list = mapper.getNewsList(map);
        sqlSession.close();
        return list;
    }
}
