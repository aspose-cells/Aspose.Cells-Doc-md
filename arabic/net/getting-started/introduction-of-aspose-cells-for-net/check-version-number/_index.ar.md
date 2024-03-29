﻿---
title: تحقق من رقم الإصدار
type: docs
weight: 80
url: /ar/net/check-version-number/
---
{{% alert color="primary" %}}

هل تتساءل عن إصدار Aspose.Cells الذي تستخدمه؟ ننشر إصدارات جديدة من Aspose.Cells ، لتقديم ميزات جديدة وإصلاح المشكلات ، على أساس منتظم. يتكون رقم الإصدار من رقم الإصدار الرئيسي ورقم الإصدار الثانوي ورقم إصدار الإصلاح العاجل. يجب أن يكون كل رقم عددًا صحيحًا من 0 إلى الأعلى. التنسيق كالتالي:

رئيسي. minor.hotfix

عندما نصدر إصدارًا جديدًا من Aspose.Cells ، نقوم بتحديث رقم الإصدار.

تشرح هذه المقالة كيفية التحقق من إصدار Aspose.Cells المثبت على النظام يدويًا واستخدام Aspose.Cells API.

{{% /alert %}}

## **تحقق من رقم الإصدار يدويًا**

لمعرفة إصدار Aspose.Cells الذي تستخدمه يدويًا:

1.  انقر بزر الماوس الأيمن فوق الملف Aspose.Cells.dll وحدد**ملكيات**.
1. انقر فوق علامة التبويب الإصدار (أو التفاصيل) للتحقق من رقم الإصدار.

## **تحقق من رقم الإصدار باستخدام Aspose.Cells API**

 لمعرفة إصدار Aspose.Cells الذي تستخدمه من خلال API ، استخدم ملف[الخلايا](https://reference.aspose.com/cells/net/aspose.cells/cellshelper) طريقة ثابتة من فئة GetVersion للحصول على رقم إصدار Aspose.Cell.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-CheckVersionNumber-1.cs" >}}
