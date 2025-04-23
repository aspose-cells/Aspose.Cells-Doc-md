---
title: Лицензирование
type: docs
weight: 50
url: /ru/go-cpp/licensing/
---

## **Ограничения оценочной версии**

A free evaluation version of Aspose.Cells for Go via C++ can be downloaded from the downloads section of Aspose's web site at: <//<https://releases.aspose.com/cells/go-cpp/>>.

## **Загрузка лицензии из файла**

{{% alert color="primary" %}}

При вызове метода SetLicense, имя лицензии, которое вы передаете, должно соответствовать имени файла лицензии. Например, если вы измените имя файла лицензии на "Aspose.Cells.lic.xml", передайте это имя файла в метод License->SetLicense_String(…).

{{% /alert %}}

**Go**

{{< highlight csharp >}}
 lic, _:= NewLicense()
 lic.SetLicense_String(os.Getenv("LicensePath"))

{{< /highlight >}}
