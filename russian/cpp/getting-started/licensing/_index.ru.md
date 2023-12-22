---
title: Licensing
type: docs
weight: 50
url: /ru/cpp/licensing/
---
##  **Ограничения ознакомительной версии**
 Бесплатную ознакомительную версию Aspose.Cells for C++ можно загрузить из раздела загрузок на веб-сайте Aspose по адресу:<https://downloads.aspose.com/cells/cpp>.
##  **Применить лицензию с помощью файла или объекта потока**
Лицензию можно загрузить из файла или потокового объекта. Aspose.Cells for C++ попытается найти лицензию в следующих местах:

1. Явный путь.
1. Папка, содержащая Aspose.Cells.dll.
1. Папка, содержащая сборку с именем Aspose.Cells.dll.
1. Папка, содержащая входную сборку (ваш .exe).
1. Встроенный ресурс в сборке с именем Aspose.Cells.dll.

Самый простой способ установить лицензию — поместить файл лицензии в ту же папку, что и файл Aspose.Cells.dll, и указать имя файла без пути, как показано в примере ниже.
###  **Загрузка лицензии из файла**
Самый простой способ применить лицензию — поместить файл лицензии в ту же папку, что и файл Aspose.Cells.dll, и указать только имя файла без пути.

{{% alert color="primary" %}} 

При вызове метода SetLicense передаваемое имя лицензии должно совпадать с именем файла лицензии. Например, если вы измените имя файла лицензии на «Aspose.Cells.lic.xml», передайте это имя файла в метод Cells->SetLicense(…).

{{% /alert %}} 

**C++**

{{< highlight "csharp" >}}
  License license;
  license.SetLicense(u"Aspose.Cells.lic");

{{< /highlight >}}
###  **Загрузка лицензии из объекта Stream**
В следующем примере показано, как загрузить лицензию из потока.

**C++**

{{< highlight "csharp" >}}

  License license;

  //You need to write your own code to read the contents of the license file into this variable.
  Vector<uint8_t> myStream{0}; //"Aspose.Cells.lic"

  license.SetLicense(myStream);

{{< /highlight >}}
