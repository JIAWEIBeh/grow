package com.example.costing.domain.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.math.BigDecimal;

@Data
@TableName("bom_item")
public class BomItem {
    @TableId(type = IdType.AUTO)
    private Long id;
    private Long productId;
    private Long materialId;
    private BigDecimal quantity;

    @TableField(exist = false)
    private Material material;
}

