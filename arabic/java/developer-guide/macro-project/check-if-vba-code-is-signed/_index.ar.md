---
title: التحقق مما إذا كان كود VBA موقع بالتوقيع
type: docs
weight: 30
url: /ar/java/check-if-vba-code-is-signed/
---

{{% alert color="primary" %}}

تسمح Aspose.Cells للمستخدم بالتحقق مما إذا كان مشروع كود VBA موقعًا أم لا. يرجى استخدام الطريقة [**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned) للتحقق مما إذا كان مشروع كود VBA موقعًا أم لا.

{{% /alert %}}

## **فحص ما إذا كان رمز VBA موقعًا**

الكود التالي يشرح كيفية التحقق مما إذا كان مشروع كود VBA موقعًا أم لا باستخدام الطريقة [**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned). يمكنك استخدام أي ملفات الإكسل الخاصة بك لاختبار هذا الكود. لأغراض الاختبار يمكنك استخدام [هذا الملف الإكسل المستخدم في الكود](5472500.xlsm).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckVBAProjectInWorkbookIsSigned-CheckVBAProjectInWorkbookIsSigned.java" >}}

## **مخرجات الوحدة**

فيما يلي مخرجات وحدة التحكم للكود أعلاه باستخدام [ملف الإكسل عينة](5472500.xlsm) الذي تم توفيره عبر الرابط.

{{< highlight java >}}

Is VBA Code Project Signed: true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
