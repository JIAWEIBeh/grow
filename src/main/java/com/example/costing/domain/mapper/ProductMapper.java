package com.example.costing.domain.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.example.costing.domain.entity.Product;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface ProductMapper extends BaseMapper<Product> {
}

