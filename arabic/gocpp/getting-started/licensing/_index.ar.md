---
title: ترخيص
type: docs
weight: 50
url: /ar/go-cpp/licensing/
---

## **قيود النسخة التقييمية**

A free evaluation version of Aspose.Cells for Go via C++ can be downloaded from the downloads section of Aspose's web site at: <//<https://releases.aspose.com/cells/go-cpp/>>.

## **تحميل ترخيص من ملف**

{{% alert color="primary" %}}

عند استدعاء طريقة SetLicense، يجب أن يكون اسم الترخيص الذي تمرره هو اسم ملف الترخيص. على سبيل المثال، إذا قمت بتغيير اسم ملف الترخيص إلى "Aspose.Cells.lic.xml"، مرر ذلك الاسم إلى طريقة License->SetLicense_String(…)

{{% /alert %}}

**جو**

{{< highlight csharp >}}
 lic, _:= NewLicense()
 lic.SetLicense_String(os.Getenv("LicensePath"))

{{< /highlight >}}
