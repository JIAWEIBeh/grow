package com.example.costing.controller;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.example.costing.domain.entity.BomItem;
import com.example.costing.service.BomItemService;
import jakarta.validation.Valid;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/bom-items")
public class BomItemController {
    private final BomItemService bomItemService;

    public BomItemController(BomItemService bomItemService) {
        this.bomItemService = bomItemService;
    }

    @GetMapping
    public Page<BomItem> list(@RequestParam(required = false) Long productId,
                              @RequestParam(defaultValue = "1") long page,
                              @RequestParam(defaultValue = "10") long size) {
        LambdaQueryWrapper<BomItem> wrapper = new LambdaQueryWrapper<>();
        if (productId != null) {
            wrapper.eq(BomItem::getProductId, productId);
        }
        return bomItemService.page(Page.of(page, size), wrapper);
    }

    @PostMapping
    public BomItem create(@Valid @RequestBody BomItem item) {
        bomItemService.save(item);
        return item;
    }

    @PutMapping("/{id}")
    public BomItem update(@PathVariable Long id, @Valid @RequestBody BomItem item) {
        item.setId(id);
        bomItemService.updateById(item);
        return bomItemService.getById(id);
    }

    @DeleteMapping("/{id}")
    public void delete(@PathVariable Long id) {
        bomItemService.removeById(id);
    }
}

