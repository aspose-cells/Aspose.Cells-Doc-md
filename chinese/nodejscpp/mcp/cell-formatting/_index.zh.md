---
title: Excel 单元格格式
linktitle: 单元格格式
type: docs
weight: 40
url: /zh/nodejs-cpp/mcp/cell-formatting
keywords: "Excel 单元格格式、Excel 单元格样式、Excel 边框、Excel 对齐、Excel 背景色、AI Excel 格式"
description: "Excel 单元格格式  通过 AI 自动化应用背景、边框、对齐、数字格式和单元格样式"
---

# Excel 单元格格式

使用基于 AI 的自动化应用专业 **Excel 单元格格式**。为 **Excel 单元格** 添加背景、边框、对齐、数字格式和高级单元格属性。

## 可用工具

- `cell_format` - 通过 **Excel MCP** 实现 **Excel 单元格格式**（背景、边框、对齐、数字格式）
- `cell_format_batch` - 使用 **AI 自动化** 批量应用 **Excel 单元格格式**

## 单元格单独格式化

### 基本单元格样式
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "reports/formatted-report.xlsx",
    "sheet_name": "Data",
    "range": "A1:F1",
    "background_color": "#4472C4",
    "horizontal_align": "center",
    "vertical_align": "middle",
    "border_style": "thick",
    "text_wrap": true
  }
}
```

### 专业标题格式
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data",
    "range": "A1:F1",
    "background_color": "#2E5984",
    "horizontal_align": "center",
    "vertical_align": "middle",
    "border_style": "thick",
    "border_color": "#000000",
    "text_wrap": true
  }
}
```

### 数字格式化
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "reports/financial.xlsx",
    "sheet_name": "Budget",
    "range": "C2:C10",
    "number_format": "$#,##0.00",
    "horizontal_align": "right"
  }
}
```

## 批量单元格格式化

### 完整报告样式
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Sheet1",
    "format_ranges": [
      {
        "range": "A1:F1",
        "background_color": "#2E5984",
        "horizontal_align": "center",
        "vertical_align": "middle",
        "border_style": "thick",
        "border_color": "#000000"
      },
      {
        "range": "B2:B4",
        "number_format": "$#,##0.00",
        "horizontal_align": "right"
      },
      {
        "range": "C2:C4",
        "number_format": "0",
        "horizontal_align": "center"
      },
      {
        "range": "D2:F5",
        "number_format": "$#,##0.00",
        "horizontal_align": "right"
      },
      {
        "range": "A5:F5",
        "border_style": "thick",
        "border_sides": ["top"]
      }
    ]
  }
}
```

### 高级边框样式
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/border-demo.xlsx",
    "sheet_name": "Sheet1",
    "format_ranges": [
      {
        "range": "A5:A7",
        "border_style": "thin",
        "border_color": "#000000",
        "border_sides": ["all"]
      },
      {
        "range": "B5:B7",
        "border_style": "medium",
        "border_color": "#FF0000",
        "border_sides": ["outline"]
      },
      {
        "range": "C5:C7",
        "border_style": "dashed",
        "border_color": "#0000FF",
        "border_sides": ["top", "bottom"]
      },
      {
        "range": "D5:D7",
        "border_style": "dotted",
        "border_color": "#00FF00",
        "border_sides": ["left", "right"]
      },
      {
        "range": "E5:E7",
        "border_style": "double",
        "border_color": "#FF00FF",
        "border_sides": ["all"]
      }
    ]
  }
}
```

### 文本对齐展示
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/alignment-demo.xlsx",
    "sheet_name": "Sheet1",
    "format_ranges": [
      {
        "range": "A10",
        "horizontal_align": "left",
        "vertical_align": "top",
        "background_color": "#FFE6E6"
      },
      {
        "range": "B10",
        "horizontal_align": "center",
        "vertical_align": "middle",
        "background_color": "#E6FFE6"
      },
      {
        "range": "C10",
        "horizontal_align": "right",
        "vertical_align": "bottom",
        "background_color": "#E6E6FF"
      },
      {
        "range": "D10",
        "horizontal_align": "justify",
        "vertical_align": "justify",
        "text_wrap": true,
        "background_color": "#FFFFE6"
      },
      {
        "range": "E10",
        "horizontal_align": "fill",
        "indent": 2,
        "background_color": "#FFE6FF"
      }
    ]
  }
}
```

### 文字旋转效果
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/rotation-demo.xlsx",
    "sheet_name": "Sheet1",
    "format_ranges": [
      {
        "range": "D1",
        "text_rotation": 45,
        "horizontal_align": "center",
        "vertical_align": "middle"
      },
      {
        "range": "E1",
        "text_rotation": -45,
        "horizontal_align": "center",
        "vertical_align": "middle"
      },
      {
        "range": "F1",
        "text_rotation": 90,
        "horizontal_align": "center",
        "vertical_align": "middle"
      }
    ]
  }
}
```

## 格式参数参考

### 背景颜色
- `"#FFFFFF"` - 白色
- `"#4472C4"` - 专业蓝
- `"#E6F3FF"` - 浅蓝色
- `"#FFFF00"` - 黄色
- `"#FFE6E6"` - 浅红色
- `"#E6FFE6"` - 浅绿色
- `"#F0F8FF"` - 爱丽丝蓝

### 水平对齐
- `"left"` - 左对齐
- `"center"` - 居中对齐
- `"right"` - 右对齐
- `"justify"` - 两端对齐
- `"fill"` - 填充单元格

### 垂直对齐
- `"top"` - 顶部对齐
- `"middle"` - 中间对齐
- `"bottom"` - 底部对齐
- `"justify"` - 垂直对齐

### 边框样式
- `"none"` - 无边框
- `"thin"` - 细线
- `"medium"` - 中线
- `"thick"` - 粗线
- `"dashed"` - 虚线
- `"dotted"` - 点线
- `"double"` - 双线

### 边框方向
- `["all"]` - 所有边
- `["top", "bottom"]` - 上下边
- `["left", "right"]` - 左右边
- `["outline"]` - 只外边框
- `["inside"]` - 只内边框

### 数字格式
- `"General"` - 通用格式
- `"0"` - 整数
- `"0.00"` - 两位小数
- `"0%"` - 百分比
- `"$#,##0.00"` - 带千位分隔符的货币
- `"yyyy-mm-dd"` - 日期格式
- `"h:mm AM/PM"` - 时间格式

### 文本属性
- `text_wrap: true` - 单元格文本换行
- `text_rotation: 45` - 文本旋转（度数）
- `indent: 2` - 文本缩进级别
- `locked: true` - 锁定单元格以保护
- `hidden: true` - 隐藏单元格公式

## 高级格式示例

### 财务报告样式
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/financial-complete.xlsx",
    "sheet_name": "Sheet1",
    "format_ranges": [
      {
        "range": "D2:D5",
        "background_color": "#F0F8FF"
      },
      {
        "range": "E2:E5",
        "background_color": "#FFF0F0"
      },
      {
        "range": "F2:F5",
        "background_color": "#F0FFF0",
        "border_style": "double",
        "border_sides": ["all"]
      }
    ]
  }
}
```

### 数据验证高亮
```json
{
  "tool": "cell_format_batch",
  "parameters": {
    "filepath": "reports/data-validation.xlsx",
    "sheet_name": "Data",
    "format_ranges": [
      {
        "range": "A2:A10",
        "background_color": "#90EE90"
      },
      {
        "range": "B2:B10",
        "background_color": "#FFB6C1"
      },
      {
        "range": "C2:C10",
        "background_color": "#87CEEB",
        "border_style": "thin",
        "border_sides": ["all"]
      }
    ]
  }
}
```

### 保护设置
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "reports/protected.xlsx",
    "sheet_name": "Sheet1",
    "range": "B1:B5",
    "locked": false,
    "hidden": true
  }
}
```

## 最佳实践

1. **色彩和谐**：使用互补色以提升专业外观
2. **对比度**：确保文本在背景色上易于阅读
3. **一致性**：在类似数据中应用一致的格式
4. **边框**：使用边框分隔区域并突出重要数据
5. **数字格式**：为不同数据类型应用合适的数字格式

## 常见用例

### 报告标题
- 深色背景白色文字
- 居中对齐
- 粗边框
- 启用自动换行

### 财务数据
- 货币格式化
- 数字右对齐
- 高亮显示负值
- 千位分隔符

### 状态指示器
- 彩色背景
- 居中对齐
- 粗边框
- 明确的视觉区分

### 数据表格
- 交替行颜色
- 一致的列宽
- 合适的数字格式
- 明确的标题样式

## 错误处理

### 无效的颜色代码
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "range": "A1",
    "background_color": "invalid-color"
  }
}
```
**结果**：使用默认背景色

### 无效数字格式
```json
{
  "tool": "cell_format",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "range": "A1",
    "number_format": "invalid-format"
  }
}
```
**结果**：采用通用格式作为备用 
{{< app/cells/assistant language="nodejs-cpp" >}}
