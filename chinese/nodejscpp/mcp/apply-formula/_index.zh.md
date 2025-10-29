---
title: Excel 公式操作  Excel 公式 MCP
linktitle: 公式操作  Excel 公式 MCP
type: docs
weight: 20
url: /zh/nodejs-cpp/mcp/apply-formula
keywords: "Excel 公式 MCP，Excel 公式，AI Excel 公式，Excel 公式自动化，Excel 计算"
description: "Excel 公式 MCP  使用 AI 自动化应用 Excel 公式，单个和批量 Excel 公式操作"
---

# Excel 公式操作

**Excel 公式 MCP** 提供强大的 **Excel 公式** 自动化与 AI 集成。将 **Excel 公式**应用于单个单元格或批量单元格操作。

## 可用工具

- `apply_formula` - 使用 **Excel 公式 MCP** 将 **Excel 公式**应用到单个单元格
- `apply_formula_batch` - 使用 **AI Excel** 批量应用 **Excel 公式**

## 单个公式操作

### 使用等号应用公式
```json
{
  "tool": "apply_formula",
  "parameters": {
    "filepath": "reports/calculations.xlsx",
    "sheet_name": "Data",
    "cell": "D2",
    "formula": "=B2*C2"
  }
}
```

### 不带等号应用公式
```json
{
  "tool": "apply_formula",
  "parameters": {
    "filepath": "reports/calculations.xlsx",
    "sheet_name": "Data",
    "cell": "E2",
    "formula": "SUM(B2:D2)"
  }
}
```

### 常用 Excel 公式
```json
{
  "tool": "apply_formula",
  "parameters": {
    "filepath": "reports/analysis.xlsx",
    "sheet_name": "Summary",
    "cell": "F2",
    "formula": "=AVERAGE(A2:E2)"
  }
}
```

## 批量公式操作

### 计算销售报告总额
```json
{
  "tool": "apply_formula_batch",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data",
    "formulas": [
      { "cell": "E2", "formula": "=C2*D2" },
      { "cell": "E3", "formula": "=C3*D3" },
      { "cell": "E4", "formula": "=C4*D4" },
      { "cell": "E5", "formula": "=SUM(E2:E4)" }
    ]
  }
}
```

### 含税计算的财务报告
```json
{
  "tool": "apply_formula_batch",
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Sheet1",
    "formulas": [
      { "cell": "D2", "formula": "=B2*C2" },
      { "cell": "D3", "formula": "=B3*C3" },
      { "cell": "D4", "formula": "=B4*C4" },
      { "cell": "E2", "formula": "=D2*0.1" },
      { "cell": "E3", "formula": "=D3*0.1" },
      { "cell": "E4", "formula": "=D4*0.1" },
      { "cell": "F2", "formula": "=D2+E2" },
      { "cell": "F3", "formula": "=D3+E3" },
      { "cell": "F4", "formula": "=D4+E4" },
      { "cell": "D5", "formula": "=SUM(D2:D4)" },
      { "cell": "E5", "formula": "=SUM(E2:E4)" },
      { "cell": "F5", "formula": "=SUM(F2:F4)" }
    ]
  }
}
```

### 混合公式语法
```json
{
  "tool": "apply_formula_batch",
  "parameters": {
    "filepath": "reports/analysis.xlsx",
    "sheet_name": "Data",
    "formulas": [
      { "cell": "F4", "formula": "=D4*2" },
      { "cell": "F5", "formula": "D5*2" },
      { "cell": "F6", "formula": "=D6*2" },
      { "cell": "G4", "formula": "=D4+10" },
      { "cell": "G5", "formula": "=D5+10" },
      { "cell": "G6", "formula": "=D6+10" },
      { "cell": "G7", "formula": "=SUM(G4:G6)" }
    ]
  }
}
```

## 常用 Excel 函数

### 数学函数
- `SUM(range)` - 计算范围内的值之和
- `AVERAGE(range)` - 计算平均值
- `MIN(range)` - 查找最小值
- `MAX(range)` - 查找最大值
- `COUNT(range)` - 统计数字单元格数

### 逻辑函数
- `IF(condition, true_value, false_value)` - 条件判断
- `AND(condition1, condition2)` - 逻辑与
- `OR(condition1, condition2)` - 逻辑或

### 文本函数
- `CONCATENATE(text1, text2)` - 连接文本
- `LEFT(text, num_chars)` - 提取左侧字符
- `RIGHT(text, num_chars)` - 提取右侧字符
- `LEN(text)` - 文本长度

## 最佳实践

1. **公式语法**：`=SUM(A1:A10)` 和 `SUM(A1:A10)` 都可以使用
2. **单元格引用**：在需要时使用绝对引用（`$A$1`）
3. **错误处理**：先用简单数据测试公式
4. **批量操作**：对多个类似公式使用批量操作
5. **公式验证**：应用公式后检查结果

## 错误处理

### 空的公式数组
```json
{
  "tool": "apply_formula_batch",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "formulas": []
  }
}
```
**结果**：空数组验证错误

### 无效公式
```json
{
  "tool": "apply_formula",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "cell": "A1",
    "formula": "=INVALID_FUNCTION(A1)"
  }
}
```
**结果**：公式语法错误
{{< app/cells/assistant language="nodejs-cpp" >}}
