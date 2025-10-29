---
title: خط وتنسيق النص في إكسل
linktitle: خط وتنسيق النص
type: docs
weight: 30
url: /ar/nodejs-cpp/mcp/font-formatting
keywords: "تنسيق خط إكسل، تنسيق نص إكسل، إعدادات خط إكسل، تصميم خطوط إكسل بالذكاء الاصطناعي، أتمتة خطوط إكسل"
description: "تنسيق خط وتنسيق نص إكسل  تطبيق أنماط الخط والألوان والأحجام وتأثيرات النص باستخدام الأتمتة بالذكاء الاصطناعي"
---

# تنسيق الخط والنص في إكسل

تطبيق تنسيق خطوط إكسل احترافي **باستخدام الأتمتة المدعومة بالذكاء الاصطناعي**. تنسيق **نص إكسل** باستخدام خطوط وألوان وأحجام وتأثيرات خاصة لموظفات بجودة عالية.

## الأدوات المتاحة

- `font_settings` - **تنسيق خط Excel** (العائلة، الحجم، الغامق، المائل، اللون، إلخ.) بدقة **AI Excel**
- `font_settings_batch` - تطبيق **إعدادات خط Excel** على نطاقات متعددة دفعة واحدة باستخدام **spreadsheet MCP**

## عمليات الخط المفرد

### تنسيق الخط الأساسي
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

### تأثيرات النص
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

### الأحرف الخاصة
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

## عمليات الخط دفعة واحدة

### تنسيق ترويسة كاملة
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

### استعراض تأثيرات النص الخاصة
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

### تنسيق تقرير مهني
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

## مرجع معلمات الخط

### عائلات الخطوط
- `"Arial"` - خط Sans-serif نظيف وحديث
- `"Calibri"` - الافتراضي في Microsoft Office
- `"Times New Roman"` - خط ذو عائلة سيريف تقليدية
- `"Arial Black"` - خط عرض سميك عريض
- `"Courier New"` - خط أحادي المسافة

### أحجام الخطوط
- `8` - نص صغير جدًا
- `10` - نص صغير
- `11` - الحجم الافتراضي
- `12` - نص الجسم القياسي
- `14` - نص كبير
- `16` - حجم العنوان
- `18` - عنوان كبير

### ألوان الخطوط (رموز هكس)
- `"#000000"` - أسود
- `"#FFFFFF"` - أبيض
- `"#FF0000"` - أحمر
- `"#0066CC"` - أزرق
- `"#006600"` - أخضر
- `"#FF6600"` - برتقالي
- `"#800080"` - بنفسجي

### تأثيرات النص
- `bold: true` - نص غامق
- `italic: true` - نص مائل
- `underline: true` - نص تحت خط
- `strikethrough: true` - نص مشطوب
- `subscript: true` - نص أسفل خط (H₂O)
- `superscript: true` - نص فوقي (x²)

## تنسيق الخط المتقدم

### مثال على التمثيل العلمي
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

### بيانات مشفرة بالألوان
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

## أفضل الممارسات

1. **الاتساق**: استخدم عائلات خطوط متناسقة في جميع التقارير
2. **التدرج الهرمي**: استخدم أحجام الخطوط لإنشاء تدرج مرئي
3. **سهولة القراءة**: تأكد من وجود تباين كافٍ بين النص والخلفية
4. **التأثيرات**: استخدم تأثيرات النص بشكل مقتصد للتأكيد
5. **احترافية**: التزم بخطوط العمل التجارية القياسية للتقارير

## حالات الاستخدام الشائعة

### رؤوس التقارير
- خط غامق أكبر حجمًا
- ألوان متباينة
- عائلات خطوط احترافية

### تأكيد البيانات
- غامق أو مائل للقيم المهمة
- الترميز اللوني لمؤشرات الحالة
- خط مشطوب للبيانات القديمة

### الوثائق العلمية
- رمز العلمي للمعادلات الكيميائية
- النص superscript للعبارات الرياضية
- الأحرف الأحادية للمحتوى البرمجي أو البيانات

## معالجة الأخطاء

### عائلة الخط غير صالحة
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
**النتيجة**: العودة إلى الخط الافتراضي للنظام

### رمز اللون غير صالح
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
**النتيجة**: يستخدم اللون الأسود الافتراضي 
{{< app/cells/assistant language="nodejs-cpp" >}}
