---
title: Excel 字体和文本格式化
linktitle: 字体和文本格式化
type: docs
weight: 30
url: /zh/nodejs-cpp/mcp/font-formatting
keywords: "Excel 字体格式化、Excel 文本格式化、Excel 字体设置、AI Excel 字体样式、Excel 字体自动化"
description: "Excel 字体与文本格式化——使用 AI 自动应用字体样式、颜色、大小和文本效果"
---

# Excel 字体与文本格式化

使用 AI 自动化应用专业的**Excel 字体格式化**。用字体、颜色、大小和特殊效果为**Excel 文本**增添风采，打造精美的电子表格。

## 可用工具

- `font_settings` - **Excel字体样式**（字体、大小、粗体、斜体、颜色等）配合 **AI Excel** 精准控制
- `font_settings_batch` - 使用 **spreadsheet MCP** 批量应用 **Excel字体设置**到多个范围

## 单个字体操作

### 基础字体样式
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "reports/styled-report.xlsx",
    "sheet_name": "Data",
    "range": "A1:F1",
    "font_name": "Arial",
    "font_size": 14,
    "bold": true,
    "font_color": "#FFFFFF"
  }
}
```

### 文字效果
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "reports/effects-demo.xlsx",
    "sheet_name": "Sheet1",
    "range": "A2",
    "italic": true,
    "underline": true,
    "strikethrough": true,
    "font_color": "#FF0000"
  }
}
```

### 特殊字符
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "reports/scientific.xlsx",
    "sheet_name": "Formulas",
    "range": "A3",
    "font_size": 10,
    "subscript": true
  }
}
```

## 批量字体操作

### 完整标题样式
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/professional-report.xlsx",
    "sheet_name": "Summary Report",
    "font_ranges": [
      {
        "range": "C3:G3",
        "font_name": "Arial Black",
        "font_size": 16,
        "bold": true,
        "italic": true,
        "underline": true,
        "font_color": "#FF0000"
      },
      {
        "range": "D4:D6",
        "font_name": "Calibri",
        "font_size": 12,
        "bold": true,
        "font_color": "#0066CC"
      },
      {
        "range": "E4:E6",
        "font_name": "Times New Roman",
        "italic": true,
        "font_color": "#006600"
      }
    ]
  }
}
```

### 特殊文本效果展示
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/text-effects.xlsx",
    "sheet_name": "Effects Demo",
    "font_ranges": [
      {
        "range": "A3",
        "font_size": 10,
        "subscript": true
      },
      {
        "range": "B3",
        "font_size": 10,
        "superscript": true
      },
      {
        "range": "C3",
        "strikethrough": true,
        "underline": true,
        "font_color": "#CC0000"
      }
    ]
  }
}
```

### 专业报告样式
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Sheet1",
    "font_ranges": [
      {
        "range": "A1:F1",
        "font_name": "Arial",
        "font_size": 14,
        "bold": true,
        "font_color": "#FFFFFF"
      },
      {
        "range": "A5:F5",
        "bold": true,
        "font_size": 12
      },
      {
        "range": "F2:F5",
        "bold": true,
        "font_color": "#006600"
      }
    ]
  }
}
```

## 字体参数参考

### 字体系列
- `"Arial"` - 简洁现代无衬线字体
- `"Calibri"` - 微软 Office 默认字体
- `"Times New Roman"` - 传统衬线字体
- `"Arial Black"` - 粗体显示字体
- `"Courier New"` - 等宽字体

### 字体大小
- `8` - 非常小的文字
- `10` - 小号文字
- `11` - 默认字号
- `12` - 标准正文
- `14` - 大号字体
- `16` - 标题大小
- `18` - 大标题

### 字体颜色（十六进制代码）
- `"#000000"` - 黑色
- `"#FFFFFF"` - 白色
- `"#FF0000"` - 红色
- `"#0066CC"` - 蓝色
- `"#006600"` - 绿色
- `"#FF6600"` - 橙色
- `"#800080"` - 紫色

### 文字效果
- `bold: true` - 加粗
- `italic: true` - 斜体
- `underline: true` - 下划线
- `strikethrough: true` - 删除线
- `subscript: true` - 下标文本（H₂O）
- `superscript: true` - 上标文本（x²）

## 高级字体样式

### 科学计数法示例
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/scientific.xlsx",
    "sheet_name": "Formulas",
    "font_ranges": [
      {
        "range": "A1",
        "font_name": "Times New Roman",
        "font_size": 12,
        "bold": true
      },
      {
        "range": "B1",
        "font_size": 10,
        "subscript": true
      },
      {
        "range": "C1",
        "font_size": 10,
        "superscript": true
      }
    ]
  }
}
```

### 颜色编码数据
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/color-coded.xlsx",
    "sheet_name": "Status Report",
    "font_ranges": [
      {
        "range": "A2:A5",
        "font_color": "#008000",
        "bold": true
      },
      {
        "range": "B2:B5",
        "font_color": "#FF8C00",
        "italic": true
      },
      {
        "range": "C2:C5",
        "font_color": "#DC143C",
        "strikethrough": true
      }
    ]
  }
}
```

## 最佳实践

1. **一致性**：在报告中使用一致的字体系列
2. **层次**：使用字体大小创建视觉层次
3. **可读性**：确保文本与背景之间有足够的对比度
4. **效果**：为强调有选择地使用文本效果
5. **专业**：报告使用标准商务字体

## 常见用例

### 报告标题
- 粗体，大字体
- 对比色
- 专业字体系列

### 数据强调
- 重要数值使用粗体或斜体
- 使用颜色编码状态指示器
- 用删除线标记废弃数据

### 科学文档
- 化学式下标
- 数学表达式的上标
- 代码或数据的等宽字体

## 错误处理

### 无效的字体系列
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "range": "A1",
    "font_name": "NonExistentFont"
  }
}
```
**结果**：回退到默认系统字体

### 无效的颜色代码
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "range": "A1",
    "font_color": "invalid-color"
  }
}
```
**结果**：使用默认黑色 
{{< app/cells/assistant language="nodejs-cpp" >}}
