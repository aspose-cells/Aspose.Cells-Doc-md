---
title: تنسيق خلايا إكسل
linktitle: تنسيق الخلايا
type: docs
weight: 40
url: /ar/nodejs-cpp/mcp/cell-formatting
keywords: "تنسيق خلايا إكسل، أنماط خلايا إكسل، حدود إكسل، محاذاة إكسل، ألوان خلفية إكسل، تنسيق إكسل باستخدام الذكاء الاصطناعي"
description: "تطبيق تنسيق خلايا إكسل  تطبيق الخلفيات، الحدود، المحاذاة، تنسيقات الأرقام، وأنماط الخلايا باستخدام أتمتة الذكاء الاصطناعي"
---

# تنسيق خلايا إكسل

تطبيق تنسيق خلايا إكسل احترافي **مدعوم بالذكاء الاصطناعي** باستخدام الأتمتة. تنسيق **خلايا إكسل** مع خلفيات، حدود، محاذاة، تنسيقات الأرقام، وخصائص خلوية متقدمة.

## الأدوات المتاحة

- `cell_format` - **تنسيق خلايا إكسل** (الخلفية، الحدود، المحاذاة، تنسيق الأرقام) عبر **نظام إدارة محتوى إكسل**
- `cell_format_batch` - تطبيق **تنسيق خلايا إكسل** على عدة نطاقات دفعة واحدة باستخدام **الأتمتة الذكية**

## تنسيق خلية واحدة

### تنسيق أساسي للخلايا
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

### تنسيق الرأس المهني
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

### تنسيق الأرقام
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

## تنسيق دفعات للخلايا

### تنسيق تقرير كامل
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

### أنماط حدود متقدمة
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

### استعراض محاذاة النص
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

### تأثيرات دوران النص
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

## مرجع معلمات التنسيق

### ألوان الخلفية
- `"#FFFFFF"` - الأبيض
- `"#4472C4"` - أزرق احترافي
- `"#E6F3FF"` - أزرق فاتح
- `"#FFFF00"` - أصفر
- `"#FFE6E6"` - أحمر فاتح
- `"#E6FFE6"` - أخضر فاتح
- `"#F0F8FF"` - أزرق أليس

### محاذاة أفقية
- `"left"` - محاذاة إلى اليسار
- `"center"` - محاذاة إلى الوسط
- `"right"` - محاذاة إلى اليمين
- `"justify"` - مبرر
- `"fill"` - ملء الخلية

### محاذاة رأسية
- `"top"` - محاذاة إلى الأعلى
- `"middle"` - محاذاة وسطية
- `"bottom"` - محاذاة إلى الأسفل
- `"justify"` - تم تبريره عمودياً

### أنماط الحدود
- `"none"` - لا يوجد حدود
- `"thin"` - خط رفيع
- `"medium"` - خط متوسط
- `"thick"` - خط سميك
- `"dashed"` - خط متقطع
- `"dotted"` - خط منقط
- `"double"` - خط مزدوج

### جوانب الحدود
- `["all"]` - جميع الجوانب
- `["top", "bottom"]` - الأعلى والأسفل
- `["left", "right"]` - اليسار واليمين
- `["outline"]` - الحدود الخارجية فقط
- `["inside"]` - الحدود الداخلية فقط

### تنسيقات الأرقام
- `"General"` - التنسيق الافتراضي
- `"0"` - عدد صحيح
- `"0.00"` - منزلتين عشريتين
- `"0%"` - نسبة مئوية
- `"$#,##0.00"` - العملة مع فاصل الآلاف
- `"yyyy-mm-dd"` - تنسيق التاريخ
- `"h:mm AM/PM"` - تنسيق الوقت

### خصائص النص
- `text_wrap: true` - التفاف النص في الخلية
- `text_rotation: 45` - تدوير النص (درجات)
- `indent: 2` - مستوى المسافة البادئة للنص
- `locked: true` - قفل الخلية للحماية
- `hidden: true` - إخفاء صيغة الخلية

## أمثلة تنسيق متقدمة

### تنسيق التقرير المالي
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

### إبراز التحقق من البيانات
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

### إعدادات الحماية
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

## أفضل الممارسات

1. **تناغم الألوان**: استخدام ألوان متكاملة للمظهر الاحترافي
2. **التباين**: ضمان قابلية قراءة النص مقابل ألوان الخلفية
3. **الاتساق**: تطبيق تنسيق متناسق عبر البيانات المماثلة
4. **الحدود**: استخدام الحدود لفصل الأقسام وتسليط الضوء على البيانات المهمة
5. **تنسيقات الأرقام**: تطبيق تنسيقات رقمية مناسبة لنوع البيانات

## حالات الاستخدام الشائعة

### رؤوس التقارير
- خلفية داكنة مع نص أبيض
- محاذاة وسطية
- حدود سميكة
- تفعيل التفاف النص

### البيانات المالية
- تنسيق العملة
- محاذاة اليمن للأرقام
- تمييز القيم السلبية
- فواصل الآلاف

### مؤشرات الحالة
- خلفيات ملونة حسب الحالة
- محاذاة وسطية
- حدود غامقة
- تمييز بصري واضح

### جداول البيانات
- ألوان الصفوف بالتناوب
- عرض الأعمدة بشكل متناسق
- تنسيقات الأرقام المناسبة
- تنسيق العنوان بشكل واضح

## معالجة الأخطاء

### رمز اللون غير صحيح
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
**النتيجة**: يستخدم لون خلفية افتراضي

### تنسيق رقم غير صحيح
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
**النتيجة**: يستخدم التنسيق العام كبديل 
{{< app/cells/assistant language="nodejs-cpp" >}}
