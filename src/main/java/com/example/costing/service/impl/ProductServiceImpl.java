package com.example.costing.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.example.costing.domain.entity.Product;
import com.example.costing.domain.mapper.ProductMapper;
import com.example.costing.service.ProductService;
import org.springframework.stereotype.Service;

@Service
public class ProductServiceImpl extends ServiceImpl<ProductMapper, Product> implements ProductService {
}

