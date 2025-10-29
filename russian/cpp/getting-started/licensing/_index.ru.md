---
title: Лицензирование
type: docs
weight: 50
url: /ru/cpp/licensing/
---

## **Ограничения оценочной версии**
A free evaluation version of Aspose.Cells for C++ can be downloaded from the downloads section of Aspose's web site at: <https://downloads.aspose.com/cells/cpp>.
## **Применение лицензии с использованием файла или объекта потока**
Лицензию можно загрузить из файла или объекта потока. Aspose.Cells for C++ попытается найти лицензию в следующих местоположениях:

1. Явный путь.
1. Папка, содержащая Aspose.Cells.dll.
1. Папка, содержащая сборку, которая вызвала Aspose.Cells.dll.
1. Папка, содержащая входную сборку (ваш .exe).
1. Встроенный ресурс в сборке, которая вызвала Aspose.Cells.dll.

Самый простой способ установить лицензию - поместить файл лицензии в ту же папку, что и файл Aspose.Cells.dll, и указать только имя файла, без пути, как показано в примере ниже.
### **Загрузка лицензии из файла**
Самый простой способ применить лицензию - поместить файл лицензии в ту же папку, что и файл Aspose.Cells.dll, и указать только имя файла без пути.

{{% alert color="primary" %}} 

При вызове метода SetLicense имя лицензии, которое вы передаете, должно соответствовать имени файла лицензии. Например, если вы измените имя файла лицензии на "Aspose.Cells.lic.xml", передайте это имя файла методу Cells->SetLicense(…).

{{% /alert %}} 

**C++**

{{< highlight csharp >}}
  License license;
  license.SetLicense(u"Aspose.Cells.lic");

{{< /highlight >}}
### **Загрузка лицензии из объекта потока**
В следующем примере показано, как загрузить лицензию из потока.

**C++**

{{< highlight csharp >}}

  License license;

  //You need to write your own code to read the contents of the license file into this variable.
  Vector<uint8_t> myStream{0}; //"Aspose.Cells.lic"

  license.SetLicense(myStream);

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
