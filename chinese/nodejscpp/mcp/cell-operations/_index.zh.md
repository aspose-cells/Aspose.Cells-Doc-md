---
title: Excel单元格操作
linktitle: 单元格操作
type: docs
weight: 60
url: /zh/nodejs-cpp/mcp/cell-operations
keywords: "Excel单元格操作，合并Excel单元格，复制粘贴Excel，Excel单元格操作，AI Excel单元格操作"
description: "Excel单元格操作  合并、复制/粘贴、清除内容，以及通过AI自动化进行先进的单元格操作"
---

# Excel单元格操作

利用AI驱动的自动化执行高级**Excel单元格操作**。合并单元格，复制粘贴操作，清除内容，以及精确操作**Excel单元格**。

## 可用工具

- `cell_operations` - **Excel单元格操作**（合并、复制/粘贴、清除）带**AI驱动**自动化
- `cell_operations_batch` - 通过**电子表格MCP**批量执行多项**Excel单元格操作**

## 单元格操作

### 合并单元格
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/merged-layout.xlsx",
    "sheet_name": "Report",
    "operation": "merge_cells",
    "range": "A1:C1"
  }
}
```

### 取消合并单元格
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/unmerged.xlsx",
    "sheet_name": "Data",
    "operation": "unmerge_cells",
    "range": "A1:C1"
  }
}
```

### 复制单元格
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/data-copy.xlsx",
    "sheet_name": "Source",
    "operation": "copy_cells",
    "source_range": "A1:D5"
  }
}
```

### 粘贴数值
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/data-copy.xlsx",
    "sheet_name": "Target",
    "operation": "paste_values",
    "destination_range": "A1"
  }
}
```

### 清除内容
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/cleanup.xlsx",
    "sheet_name": "Data",
    "operation": "clear_contents",
    "range": "A1:Z100"
  }
}
```

## 批量单元格操作

### 完成合并与复制工作流程
```json
{
  "tool": "cell_operations_batch", 
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Sheet1",
    "operations": [
      {
        "operation": "merge_cells",
        "range": "A7:C7"
      },
      {
        "operation": "paste_values",
        "source_range": "A1:F1",
        "destination_range": "A9"
      },
      {
        "operation": "paste_formats",
        "source_range": "A1:F1", 
        "destination_range": "A12"
      }
    ]
  }
}
```

### 跨表操作
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/multi-sheet.xlsx",
    "sheet_name": "Summary",
    "operation": "paste_values",
    "source_range": "A1:F5",
    "source_sheet": "Data",
    "destination_range": "A1"
  }
}
```

### 数据清理操作
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/cleanup-demo.xlsx",
    "sheet_name": "Data",
    "operations": [
      {
        "operation": "clear_contents",
        "range": "A1:A10"
      },
      {
        "operation": "clear_formats",
        "range": "B1:B10"
      },
      {
        "operation": "clear_all",
        "range": "C1:C10"
      }
    ]
  }
}
```

## 操作类型参考

### 合并操作
- `merge_cells` - 将单元格合并为一个单元格
- `unmerge_cells` - 将合并单元格拆分回单个单元格
- `merge_across` - 跨行合并单元格，但保持行分隔

### 复制/粘贴操作
- `copy_cells` - 复制单元格范围到剪贴板
- `paste_values` - 只粘贴数值（不包括格式或公式）
- `paste_formulas` - 只粘贴公式（不包括数值或格式）
- `paste_formats` - 只粘贴格式（不包括数值或公式）
- `transpose_paste` - 转置粘贴（行↔列）

### 清除操作
- `clear_contents` - 清空单元格内容（保留格式）
- `clear_formats` - 清除单元格格式（保留内容）
- `clear_all` - 同时清除内容和格式

## 高级示例

### 报告标题设置
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/title-report.xlsx",
    "sheet_name": "Report",
    "operations": [
      {
        "operation": "merge_cells",
        "range": "A1:F1"
      },
      {
        "operation": "merge_cells",
        "range": "A2:F2"
      },
      {
        "operation": "merge_cells",
        "range": "A3:C3"
      },
      {
        "operation": "merge_cells",
        "range": "D3:F3"
      }
    ]
  }
}
```

### 数据模版创建
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "templates/data-template.xlsx",
    "sheet_name": "Template",
    "operations": [
      {
        "operation": "copy_cells",
        "source_range": "A1:F1"
      },
      {
        "operation": "paste_formats",
        "destination_range": "A10"
      },
      {
        "operation": "paste_formats",
        "destination_range": "A20"
      },
      {
        "operation": "paste_formats",
        "destination_range": "A30"
      }
    ]
  }
}
```

### 数据合并
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/consolidated.xlsx",
    "sheet_name": "Summary",
    "operations": [
      {
        "operation": "paste_values",
        "source_range": "A1:E10",
        "source_sheet": "Q1Data",
        "destination_range": "A2"
      },
      {
        "operation": "paste_values",
        "source_range": "A1:E10",
        "source_sheet": "Q2Data", 
        "destination_range": "A12"
      },
      {
        "operation": "paste_values",
        "source_range": "A1:E10",
        "source_sheet": "Q3Data",
        "destination_range": "A22"
      }
    ]
  }
}
```

### 公式与格式分离
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/separated.xlsx",
    "sheet_name": "Analysis",
    "operations": [
      {
        "operation": "paste_formulas",
        "source_range": "A1:F10",
        "source_sheet": "Calculations",
        "destination_range": "A1"
      },
      {
        "operation": "paste_formats",
        "source_range": "A1:F10", 
        "source_sheet": "Formatting",
        "destination_range": "A1"
      }
    ]
  }
}
```

## 跨工作表操作

### 跨工作表复制
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/multi-sheet-copy.xlsx",
    "sheet_name": "Destination",
    "operation": "paste_values",
    "source_range": "A1:D10",
    "source_sheet": "Source",
    "destination_range": "B2"
  }
}
```

### 创建汇总表
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/summary-creation.xlsx",
    "sheet_name": "Summary",
    "operations": [
      {
        "operation": "paste_values",
        "source_range": "A1:C5",
        "source_sheet": "January",
        "destination_range": "A2"
      },
      {
        "operation": "paste_values",
        "source_range": "A1:C5",
        "source_sheet": "February",
        "destination_range": "E2"
      },
      {
        "operation": "paste_values",
        "source_range": "A1:C5",
        "source_sheet": "March",
        "destination_range": "I2"
      }
    ]
  }
}
```

## 数据转换

### 转置数据
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/transposed.xlsx",
    "sheet_name": "Data",
    "operation": "transpose_paste",
    "source_range": "A1:E5",
    "destination_range": "G1"
  }
}
```

### 仅复制值
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/values-only.xlsx",
    "sheet_name": "Clean Data",
    "operations": [
      {
        "operation": "copy_cells",
        "source_range": "A1:F20",
        "source_sheet": "Raw Data"
      },
      {
        "operation": "paste_values",
        "destination_range": "A1"
      }
    ]
  }
}
```

## 最佳实践

1. **策略性合并**：合并用于标题和注释区，而非数据区域
2. **复制后粘贴**：在粘贴操作前务必复制源区域
3. **适当清除**：选择合适的清除操作以满足需求
4. **跨工作表规划**：规划多工作表操作以避免冲突
5. **批量操作**：将相关操作进行分组以提升性能

## 常见用例

### 报告标题
- 合并单元格以设定标题
- 复制标题样式
- 应用一致的样式

### 数据清理
- 清除过时内容
- 移除格式
- 重置单元格状态

### 模板创建
- 复制格式化样式
- 粘贴结构不含数据
- 创建可复用的布局

### 数据合并
- 合并多个工作表的数据
- 仅粘贴数值以避免公式冲突
- 转置数据方向

## 错误处理

### 无效合并范围
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "merge_cells",
    "range": "A1"
  }
}
```
**结果**：错误 - 无法合并单个单元格

### 丢失源范围
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "paste_values",
    "destination_range": "A1"
  }
}
```
**结果**：错误 - 无可用复制数据

### 无效的工作表引用
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "paste_values",
    "source_range": "A1:B2",
    "source_sheet": "NonExistentSheet",
    "destination_range": "A1"
  }
}
```
**结果**：错误 - 未找到源工作表 
{{< app/cells/assistant language="nodejs-cpp" >}}
