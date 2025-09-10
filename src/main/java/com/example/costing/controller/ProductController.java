package com.example.costing.controller;

import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.example.costing.domain.entity.Product;
import com.example.costing.service.ProductService;
import jakarta.validation.Valid;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/products")
public class ProductController {
    private final ProductService productService;

    public ProductController(ProductService productService) {
        this.productService = productService;
    }

    @GetMapping
    public Page<Product> list(@RequestParam(defaultValue = "1") long page,
                              @RequestParam(defaultValue = "10") long size) {
        return productService.page(Page.of(page, size));
    }

    @PostMapping
    public Product create(@Valid @RequestBody Product product) {
        productService.save(product);
        return product;
    }

    @PutMapping("/{id}")
    public Product update(@PathVariable Long id, @Valid @RequestBody Product product) {
        product.setId(id);
        productService.updateById(product);
        return productService.getById(id);
    }

    @DeleteMapping("/{id}")
    public void delete(@PathVariable Long id) {
        productService.removeById(id);
    }
}

