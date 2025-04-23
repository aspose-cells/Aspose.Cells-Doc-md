---
title: التحقق من كلمة مرور الملفات المشفرة
type: docs
weight: 10
url: /ar/java/verify-password-of-encrypted-excel-and-ods-files/
description: تحقق من كلمة مرور ملفات إكسل المشفرة (xlsx, xlsb, xls, xlsm) وملفات Open office (ODS) باستخدام رموز Java.
---

{{% alert color="primary" %}}
إذا تم قفل ملفات إكسل (xlsx، xlsb، xls، xlsm) و Open office (ODS) بكلمة مرور، Aspose.Cells for Java تدعم التحقق من كلمة المرور البسيطة دون تحليل بيانات معينة في الملفات.
{{% /alert %}}

## **تحقق من كلمة المرور للملف المُشفر**

للتحقق من كلمة مرور الملف المشفر، يوفر Aspose.Cells for Java الطريقة [**VerifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword-java.io.InputStream-java.lang.String-). تقبل الطرق معلمتين، تيار الملف وكلمة المرور التي ينبغي التحقق منها.
يوضح مقتطف الشيفرة التالي استخدام الطريقة [**VerifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword-java.io.InputStream-java.lang.String-) للتحقق مما إذا كانت كلمة المرور المقدمة صالحة أم لا.

### **كود عينة:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-VerifyPassword-1.java" >}}

{{< app/cells/assistant language="java" >}}
