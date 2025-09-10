package com.example.costing.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.example.costing.domain.entity.BomItem;
import com.example.costing.domain.mapper.BomItemMapper;
import com.example.costing.service.BomItemService;
import org.springframework.stereotype.Service;

@Service
public class BomItemServiceImpl extends ServiceImpl<BomItemMapper, BomItem> implements BomItemService {
}

