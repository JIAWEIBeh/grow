package com.example.costing.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.example.costing.domain.entity.Material;
import com.example.costing.domain.mapper.MaterialMapper;
import com.example.costing.service.MaterialService;
import org.springframework.stereotype.Service;

@Service
public class MaterialServiceImpl extends ServiceImpl<MaterialMapper, Material> implements MaterialService {
}

