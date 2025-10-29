---
title: Excel行列操作
linktitle: 行列操作
type: docs
weight: 50
url: /zh/nodejs-cpp/mcp/row-column-operations
keywords: "Excel行操作，Excel列操作，Excel布局管理，插入行，删除列，调整Excel单元格大小"
description: "Excel行列操作——使用AI自动化插入、删除、调整尺寸、隐藏/显示行列"
---

# Excel行列操作

利用AI自动化管理**Excel行和列操作**。插入、删除、调整大小、隐藏/显示**Excel行**和**列**，实现完美的电子表格布局管理。

## 可用工具

- `row_column_operations` - **Excel行/列操作**（插入、删除、调整大小、隐藏/显示），配合**AI Excel**
- `row_column_operations_batch` - 使用**Excel MCP**批量执行多项**Excel行/列操作**

## 单独操作

### 插入行
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/layout-test.xlsx",
    "sheet_name": "Data",
    "operation": "insert_rows",
    "rows": "5",
    "count": 2
  }
}
```

### 删除列
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/cleanup.xlsx",
    "sheet_name": "Sheet1",
    "operation": "delete_columns",
    "columns": "C:D"
  }
}
```

### 设置行高
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/formatted.xlsx",
    "sheet_name": "Report",
    "operation": "set_row_height",
    "rows": "1",
    "height": 30
  }
}
```

### 设置列宽
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/formatted.xlsx",
    "sheet_name": "Report",
    "operation": "set_column_width",
    "columns": "A:F",
    "width": 15
  }
}
```

## 批量操作

### 综合布局设置
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/professional-layout.xlsx",
    "sheet_name": "Summary Report",
    "operations": [
      {
        "operation": "set_row_height",
        "rows": "3",
        "height": 30
      },
      {
        "operation": "set_row_height",
        "rows": "4:6",
        "height": 20
      },
      {
        "operation": "set_column_width",
        "columns": "C",
        "width": 20
      },
      {
        "operation": "set_column_width",
        "columns": "D:G",
        "width": 15
      },
      {
        "operation": "auto_fit_rows",
        "rows": "7:10"
      }
    ]
  }
}
```

### 插入和删除操作
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/restructure.xlsx",
    "sheet_name": "Sheet1",
    "operations": [
      {
        "operation": "insert_rows",
        "rows": "5",
        "count": 2
      },
      {
        "operation": "insert_columns",
        "columns": "D",
        "count": 1
      },
      {
        "operation": "delete_rows",
        "rows": "8:9"
      }
    ]
  }
}
```

### 隐藏与取消隐藏操作
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/visibility.xlsx",
    "sheet_name": "Sheet1",
    "operations": [
      {
        "operation": "hide_rows",
        "rows": "15:16"
      },
      {
        "operation": "hide_columns",
        "columns": "H:I"
      },
      {
        "operation": "unhide_rows",
        "rows": "15"
      },
      {
        "operation": "unhide_columns",
        "columns": "H"
      }
    ]
  }
}
```

### 自动调整操作
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/auto-sized.xlsx",
    "sheet_name": "Data",
    "operations": [
      {
        "operation": "auto_fit_columns",
        "columns": "A:F"
      },
      {
        "operation": "auto_fit_rows",
        "rows": "1:20"
      }
    ]
  }
}
```

## 操作类型参考

### 插入操作
- `insert_rows` - 在指定位置插入新行
- `insert_columns` - 在指定位置插入新列

### 删除操作  
- `delete_rows` - 删除指定行
- `delete_columns` - 删除指定列

### 调整大小操作
- `set_row_height` - 设置特定行高（以点为单位）
- `set_column_width` - 设置特定列宽（以字符为单位）
- `auto_fit_rows` - 自动调整行以适应内容高度
- `auto_fit_columns` - 自动调整列以适应内容宽度

### 可见性操作
- `hide_rows` - 隐藏指定行
- `unhide_rows` - 显示隐藏的行
- `hide_columns` - 隐藏指定列
- `unhide_columns` - 显示隐藏的列

## 区间规格

### 行区间
- `"1"` - 单行（第1行）
- `"1:3"` - 行区间（第1到第3行）
- `"5:10"` - 多个连续行

### 列区间
- `"A"` - 单列（A列）
- `"A:C"` - 列区间（A到C列）
- `"D:F"` - 多个连续列

## 高级示例

### 报告标题设置
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/header-setup.xlsx",
    "sheet_name": "Report",
    "operations": [
      {
        "operation": "set_row_height",
        "rows": "1:2",
        "height": 35
      },
      {
        "operation": "set_column_width",
        "columns": "A",
        "width": 25
      },
      {
        "operation": "set_column_width",
        "columns": "B:E",
        "width": 12
      },
      {
        "operation": "set_column_width",
        "columns": "F",
        "width": 18
      }
    ]
  }
}
```

### 数据表布局
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/data-table.xlsx",
    "sheet_name": "Data",
    "operations": [
      {
        "operation": "insert_rows",
        "rows": "1",
        "count": 1
      },
      {
        "operation": "set_row_height",
        "rows": "1",
        "height": 25
      },
      {
        "operation": "auto_fit_columns",
        "columns": "A:J"
      },
      {
        "operation": "set_row_height",
        "rows": "2:100",
        "height": 18
      }
    ]
  }
}
```

### 展示布局
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/presentation.xlsx",
    "sheet_name": "Summary",
    "operations": [
      {
        "operation": "hide_columns",
        "columns": "B:C"
      },
      {
        "operation": "hide_rows",
        "rows": "10:15"
      },
      {
        "operation": "set_column_width",
        "columns": "A",
        "width": 30
      },
      {
        "operation": "set_column_width",
        "columns": "D:G",
        "width": 15
      }
    ]
  }
}
```

## 测量指南

### 行高（点）
- `15` - 默认行高
- `20` - 稍高一些，便于阅读
- `25` - 标题用好
- `30` - 大标题
- `40` - 特大用于标题

### 列宽（字符）
- `8` - 狭窄列（日期，代码）
- `12` - 标准数据列
- `15` - 中等文本列
- `20` - 宽文本列
- `25` - 额外宽，用于描述
- `30` - 超宽，用于长文本

## 最佳实践

1. **标题大小**：使标题更高更宽以增强强调
2. **数据一致性**：保持数据行的行高一致
3. **自动适应**：使用自动适应以满足动态内容大小
4. **隐藏未用**：隐藏空行空列以使外观更整洁
5. **合理分组**：将相关的调整操作批量进行

## 常用模板

### 报告设置模板
1. 在顶部插入标题行
2. 设置标题行高度
3. 自动适应数据列宽
4. 设置标准数据行高
5. 隐藏未使用区域

### 数据导入模式
1. 插入行以添加新数据
2. 自动调整列宽至内容
3. 标准化行高
4. 隐藏计算列

### 演示模式
1. 隐藏详细行/列
2. 放大汇总区域
3. 设定适合演示的尺寸
4. 仅显示相关数据

## 错误处理

### 无效行范围
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1", 
    "operation": "set_row_height",
    "rows": "0",
    "height": 20
  }
}
```
**结果**：错误 - 行号从1开始

### 无效列范围
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "set_column_width", 
    "columns": "ZZ",
    "width": 10
  }
}
```
**结果**：可能成功但超出常规使用范围

### 缺少必需参数
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "set_row_height",
    "rows": "1"
  }
}
```
**结果**：错误 - 需要高度参数 
{{< app/cells/assistant language="nodejs-cpp" >}}
