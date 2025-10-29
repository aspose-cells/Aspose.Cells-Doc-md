---
title: عمليات معادلة Excel  شهادة MCP لصرح معادلة Excel
linktitle: عمليات الصيغة  صيغة إكسل MCP
type: docs
weight: 20
url: /ar/nodejs-cpp/mcp/apply-formula
keywords: "صيغة إكسل MCP، صيغ إكسل، صيغ إكسل باستخدام الذكاء الاصطناعي، أتمتة صيغ إكسل، حسابات إكسل"
description: "صيغة إكسل MCP  تطبيق صيغ إكسل مع أتمتة الذكاء الاصطناعي، عمليات صيغة إكسل فردية والدُفعات"
---

# عمليات صيغة إكسل

**Excel Formula MCP** يوفر أتمتة قوية **لصيغة إكسل** مع تكامل الذكاء الاصطناعي. تطبيق **صيغة إكسل** على خلايا فردية أو متعددة في عمليات دفعة.

## الأدوات المتاحة

- `apply_formula` - تطبيق **صيغة إكسل** على خلايا فردية باستخدام **Excel Formula MCP**
- `apply_formula_batch` - تطبيق **صيغة إكسل** على خلايا متعددة في دفعة باستخدام **AI Excel**

## عمليات صيغة فردية

### تطبيق الصيغة بعلامة يساوي
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

### تطبيق الصيغة بدون علامة يساوي
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

### الصيغ الشائعة في إكسل
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

## عمليات دفعة للصيغ

### حساب إجمالي تقرير المبيعات
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

### تقرير مالي مع حساب الضرائب
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

### صياغة مختلطة للصيغة
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

## دوال إكسل الشائعة

### الدوال الرياضية
- `SUM(range)` - جمع القيم في النطاق
- `AVERAGE(range)` - حساب المتوسط
- `MIN(range)` - اعثر على أدنى قيمة
- `MAX(range)` - اعثر على أقصى قيمة
- `COUNT(range)` - عد الخلايا الرقمية

### الدوال المنطقية
- `IF(condition, true_value, false_value)` - المنطق الشرطي
- `AND(condition1, condition2)` - والمنطق AND
- `OR(condition1, condition2)` - والمنطق OR

### الدوال النصية
- `CONCATENATE(text1, text2)` - دمج النصوص
- `LEFT(text, num_chars)` - استخراج الأحرف اليسرى
- `RIGHT(text, num_chars)` - استخراج الأحرف اليمنى
- `LEN(text)` - طول النص

## أفضل الممارسات

1. **صياغة الصيغة**: كلا من `=SUM(A1:A10)` و `SUM(A1:A10)` يعملان
2. **مراجع الخلايا**: استخدم المراجع المطلقة (`$A$1`) عند الحاجة
3. **معالجة الأخطاء**: اختبر الصيغ باستخدام بيانات بسيطة أولاً
4. **العمليات الجماعية**: استخدم العمليات الجماعية للصيغ المتعددة المشابهة
5. **التحقق من الصيغ**: تحقق من النتائج بعد تطبيق الصيغ

## معالجة الأخطاء

### مصفوفة الصيغ الفارغة
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
**النتيجة**: خطأ في التحقق من الصحة لمصفوفة فارغة

### صيغة غير صالحة
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
**النتيجة**: خطأ في بناء جملة الصيغة
{{< app/cells/assistant language="nodejs-cpp" >}}
