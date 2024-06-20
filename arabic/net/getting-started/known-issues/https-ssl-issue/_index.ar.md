---
title: مشكلة HTTPS SSL
type: docs
weight: 20
url: /ar/net/https-ssl-issue/
---

## **مشكلة HTTPS/SSL**
أبلغ بعض المستخدمين أنهم واجهوا مشاكل في تنزيل ملفات Excel التي تم إنشاؤها باستخدام Aspose.Cells. عندما يفتح مربع الحفظ، يحتوي اسم الملف على اسم صفحة aspx بدلاً من ملف Excel، ونوع الملف فارغ.
### **تفسير**
قمنا بتغيير رؤوس الاستجابة HTTP لحل مشكلة ضغط HTTP. قد يسبب هذا مشكلة أثناء إرسال الملفات إلى متصفح العميل عبر HTTPS/SSL.
### **الحل**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPSSSLIssue.aspx-SSLIssue.cs" >}}
