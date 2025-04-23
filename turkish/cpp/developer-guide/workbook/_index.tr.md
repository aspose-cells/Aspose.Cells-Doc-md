---
title: Çalışma Kitabını C++ ile Yönetin
linktitle: Çalışma Kitabı
type: docs
weight: 60
url: /tr/cpp/managing-workbooks-and-worksheets/
description: Aspose.Cells for C++ API leri aracılığıyla Çalışma Kitabını Nasıl Yöneteceğinizi Öğrenin.
keywords: C++ ile Çalışma Kitabını Nasıl Yöneteceğinizi, Çalışma Kitabı ve sayfalarını yönetin, Çalışma kitabı ve sayfalar üzerinde çalışın.
---

{{% alert color="primary" %}}

Aspose.Cells for C++, çalışma kitaplarını ve sayfalarını yönetmek için güçlü ve esnek API sağlar. Bu bölüm, çalışma kitaplarını ve sayfalarını programlı olarak nasıl oluşturacağınızı, açacağınızı ve üzerinde işlem yapacağınızı açıklar.

{{% /alert %}}

## **Yeni Bir Çalışma Kitabı Oluşturma**
Yeni bir çalışma kitabı oluşturmak için:

Aşağıdaki adımlar, Aspose.Cells API'sini kullanarak Hello World uygulamasını oluşturur:
2. [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) sınıfını kullanarak çalışma kitabına çalışma sayfaları ekleyin.
3. [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) metodunu kullanarak çalışma kitabını kaydedin.

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Create a new workbook
    Aspose::Cells::Workbook workbook;

    // Add a worksheet to the workbook
    workbook.GetWorksheets().Add();

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

## **Varolan Bir Çalışma Kitabını Açma**
Varolan bir çalışma kitabını açmak için:

1. [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfının bir örneğini oluşturun ve dosya yolunu yapıcıya geçirin.
2. [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) sınıfını kullanarak çalışma sayfalarına erişin.
3. Gerekirse çalışma kitabını düzenleyin.
4. [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) metodunu kullanarak çalışma kitabını kaydedin.

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Workbook workbook("input.xlsx");
    auto worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).SetValue("Hello, World!");
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **Sayfaları Yönetin**
Aspose.Cells for C++, sayfaları yönetmek için ekleme, silme ve yeniden adlandırma gibi geniş bir metod yelpazesi sunar.

### **Çalışma Sayfası Ekleme**
Yeni bir çalışma sayfası eklemek için:

1. Çalışma kitabından [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) sınıfına erişin.
2. Yeni bir çalışma sayfası eklemek için [Add](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) yöntemini kullanın.

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Create a new workbook
    Aspose::Cells::Workbook workbook;

    // Add a new worksheet
    workbook.GetWorksheets().Add("NewSheet");

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

### **Bir Çalışma Sayfasını Kaldırmak**
Çalışma sayfasını kaldırmak için:

1. Çalışma kitabından [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) sınıfına erişin.
2. Bir çalışma sayfasını dizinle kaldırmak için [RemoveAt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat/) yöntemini kullanın.

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Open an existing workbook
    Aspose::Cells::Workbook workbook("input.xlsx");

    // Remove the first worksheet
    workbook.GetWorksheets().RemoveAt(0);

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

### **Çalışma Sayfasını Yeniden Adlandırma**
Çalışma sayfasının adını değiştirmek için:

1. Çalışma kitabından [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfına erişin.
2. Çalışma sayfasının adını değiştirmek için [SetName](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setname/) yöntemini kullanın.

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Workbook workbook("input.xlsx");
    auto worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName("RenamedSheet");
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **Sonuç**
Aspose.Cells for C++, çalışma kitapları ve çalışma sayfalarını yönetmek için kapsamlı araçlar sunar. İster yeni bir çalışma kitabı oluşturmanız, ister mevcut birini açmanız veya çalışma sayfalarını manipüle etmeniz gereketsin, Aspose.Cells Excel dosyalarıyla programlı olarak çalışmayı kolaylaştırır.
