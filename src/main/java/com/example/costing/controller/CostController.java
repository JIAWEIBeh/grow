package com.example.costing.controller;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.example.costing.domain.entity.BomItem;
import com.example.costing.domain.entity.Material;
import com.example.costing.service.BomItemService;
import com.example.costing.service.MaterialService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.math.BigDecimal;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/cost")
public class CostController {
    private final BomItemService bomItemService;
    private final MaterialService materialService;

    public CostController(BomItemService bomItemService, MaterialService materialService) {
        this.bomItemService = bomItemService;
        this.materialService = materialService;
    }

    @GetMapping("/product")
    public Map<String, Object> calculateProductCost(@RequestParam Long productId) {
        List<BomItem> items = bomItemService.list(new LambdaQueryWrapper<BomItem>().eq(BomItem::getProductId, productId));
        BigDecimal total = BigDecimal.ZERO;
        for (BomItem item : items) {
            Material material = materialService.getById(item.getMaterialId());
            BigDecimal line = material.getUnitCost().multiply(item.getQuantity());
            total = total.add(line);
        }
        Map<String, Object> resp = new HashMap<>();
        resp.put("productId", productId);
        resp.put("bomLines", items.size());
        resp.put("totalCost", total);
        return resp;
    }
}

