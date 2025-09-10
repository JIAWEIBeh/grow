package com.example.costing.domain.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.example.costing.domain.entity.BomItem;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface BomItemMapper extends BaseMapper<BomItem> {
}

