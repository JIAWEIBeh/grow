package com.example.costing.domain.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.math.BigDecimal;

@Data
@TableName("material")
public class Material {
    @TableId(type = IdType.AUTO)
    private Long id;
    private String code;
    private String name;
    private String unit;
    private BigDecimal unitCost;
}

