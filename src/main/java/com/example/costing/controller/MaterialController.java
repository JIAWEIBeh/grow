package com.example.costing.controller;

import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.example.costing.domain.entity.Material;
import com.example.costing.service.MaterialService;
import jakarta.validation.Valid;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/materials")
public class MaterialController {
    private final MaterialService materialService;

    public MaterialController(MaterialService materialService) {
        this.materialService = materialService;
    }

    @GetMapping
    public Page<Material> list(@RequestParam(defaultValue = "1") long page,
                               @RequestParam(defaultValue = "10") long size) {
        return materialService.page(Page.of(page, size));
    }

    @PostMapping
    public Material create(@Valid @RequestBody Material material) {
        materialService.save(material);
        return material;
    }

    @PutMapping("/{id}")
    public Material update(@PathVariable Long id, @Valid @RequestBody Material material) {
        material.setId(id);
        materialService.updateById(material);
        return materialService.getById(id);
    }

    @DeleteMapping("/{id}")
    public void delete(@PathVariable Long id) {
        materialService.removeById(id);
    }
}

