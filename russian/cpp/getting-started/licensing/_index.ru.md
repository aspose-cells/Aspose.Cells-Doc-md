---
title: Лицензирование
type: docs
weight: 50
url: /ru/cpp/licensing/
---
## **Ограничения ознакомительной версии**
 Бесплатную ознакомительную версию Aspose.Cells для C++ можно загрузить из раздела загрузок веб-сайта Aspose по адресу:<https://downloads.aspose.com/cells/cpp>.
## **Применить лицензию с помощью файлового или потокового объекта**
Лицензия может быть загружена из файла или потокового объекта. Aspose.Cells для C++ попытается найти лицензию в следующих местах:

1. Явный путь.
1. Папка, содержащая Aspose.Cells.dll.
1. Папка, содержащая сборку с именем Aspose.Cells.dll.
1. Папка, содержащая сборку записи (ваш .exe).
1. Встроенный в сборку ресурс, вызывающий Aspose.Cells.dll.

Самый простой способ установить лицензию — поместить файл лицензии в ту же папку, что и файл Aspose.Cells.dll, и указать имя файла без пути, как показано в примере ниже.
### **Загрузка лицензии из файла**
Самый простой способ применить лицензию — поместить файл лицензии в ту же папку, что и файл Aspose.Cells.dll, и указать только имя файла без пути.

{{% alert color="primary" %}} 

При вызове метода SetLicense имя лицензии, которое вы передаете, должно совпадать с именем файла лицензии. Например, если вы измените имя файла лицензии на «Aspose.Cells.lic.xml», передайте это имя файла методу Cells->SetLicense(…).

{{% /alert %}} 

**C++**

{{< highlight "csharp" >}}

 intrusive_ptr<License> license = new License();

license->SetLicense(new String("Aspose.Cells.lic"));

{{< /highlight >}}
### **Загрузка лицензии из потокового объекта**
В следующем примере показано, как загрузить лицензию из потока.

**C++**

{{< highlight "csharp" >}}

 intrusive_ptr<License>license = new License();

intrusive_ptr<FileStream> myStream = new FileStream(new String("Aspose.Cells.lic"), FileMode_Open);

license->SetLicense(myStream);

{{< /highlight >}}
