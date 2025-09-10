INSERT INTO material (code, name, unit, unit_cost) VALUES
 ('M001', 'Steel', 'kg', 5.2000),
 ('M002', 'Plastic', 'kg', 2.5000),
 ('M003', 'Screw', 'pcs', 0.0300);

INSERT INTO product (code, name) VALUES
 ('P100', 'Widget A'),
 ('P200', 'Widget B');

-- BOM for Widget A
INSERT INTO bom_item (product_id, material_id, quantity) VALUES
 (1, 1, 2.5),
 (1, 2, 1.2),
 (1, 3, 10);

-- BOM for Widget B
INSERT INTO bom_item (product_id, material_id, quantity) VALUES
 (2, 1, 1.0),
 (2, 3, 6);

