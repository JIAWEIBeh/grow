# 成本核算系统原型

基于 Java Spring Boot + MyBatis-Plus + H2 内存库，前端为静态 Vue2（使用 iView 与 vxe-table）。

## 运行

- JDK 17
- Maven 3.8+

```bash
mvn spring-boot:run
```

启动后访问：
- 前端页面：`http://localhost:8080/`
- H2 控制台：`http://localhost:8080/h2-console`（JDBC URL: `jdbc:h2:mem:costingdb`，用户名 `sa`，密码留空）
- OpenAPI 文档：`http://localhost:8080/swagger-ui/index.html`

## API 概览

- `GET /api/materials` 查询物料分页
- `POST /api/materials` 新增物料
- `PUT /api/materials/{id}` 更新物料
- `DELETE /api/materials/{id}` 删除物料

- `GET /api/products` 查询产品分页
- `POST /api/products` 新增产品
- `PUT /api/products/{id}` 更新产品
- `DELETE /api/products/{id}` 删除产品

- `GET /api/bom-items?productId=...` 查询 BOM 明细
- `POST /api/bom-items` 新增 BOM 行
- `PUT /api/bom-items/{id}` 更新 BOM 行
- `DELETE /api/bom-items/{id}` 删除 BOM 行

- `GET /api/cost/product?productId=...` 计算产品成本（Σ 数量 × 物料单价）

## 说明

- 使用 H2 内存数据库，应用启动自动执行 `schema.sql` 与 `data.sql`，内置示例数据。
- 前端为单文件 `src/main/resources/static/index.html`，通过 axios 调用后端接口。
- 已开启全局 CORS。

## 技术栈

- 后端：Spring Boot 3、MyBatis-Plus、H2、springdoc-openapi
- 前端：Vue 2、iView、vxe-table（均通过 CDN 引入）