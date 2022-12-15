---
title: Başlarken
type: docs
weight: 10
url: /tr/cpp/getting-started/
description: Aspose Cells for C++ nasıl kurulur ve Hello World uygulaması nasıl oluşturulur.
---
{{% alert color="primary" %}} 

Bu sayfa size Aspose Cells for C++'i nasıl kuracağınızı ve Hello World uygulamasını nasıl oluşturacağınızı gösterecek.

{{% /alert %}}

## **Kurulum**

### **Aspose Cells ila NuGet'i yükleyin**

NuGet Aspose.Cells for C++ indirip kurmanın en kolay yolu.
1. Bir Microsoft Visual Studio projesi for C++ oluşturun.
2. "Aspose.Cells.h" başlık dosyasını ekleyin.
3. Microsoft Visual Studio ve NuGet paket yöneticisini açın.
 4. İstediğiniz Aspose.Cells for C++'i bulmak için "aspose.cells.cpp" araması yapın.
5. "Yükle"ye tıklayın, Aspose.Cells for C++ indirilecek ve projenizde referans gösterilecektir.

**![Aspose Cells ila NuGet'i yükleyin](InstallThroughNuget.png)**

 aspose.cells için nuget web sayfasından da indirebilirsiniz:
[Aspose.Cells for C++ NuGet Paket](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[Ayrıntılar için daha fazla adım](/cells/tr/cpp/installation/)

### **Aspose.Cells for C++'i Windows'de kullanmak için bir demo**

1. Aşağıdaki sayfadan Aspose.Cells for C++'i indirin:
[İndir Aspose.Cells for C++(Windows)](https://downloads.aspose.com/cells/cpp/)
2. Paketi açın ve Aspose.Cells for C++'in nasıl kullanılacağına dair bir Demo bulacaksınız.
3. Demo.sln dosyasını Visual Studio 2017 veya daha yüksek sürümle açın
4. main.cpp: bu dosya test etmek için nasıl kod yazılacağını gösterir Aspose.Cells for C++
 5. sourceFile/resultFile: bu iki klasör main.cpp'de kullanılan depolama dizinleridir.

### **Linux işletim sisteminde Aspose.Cells for C++ nasıl kullanılır?**

1. Aşağıdaki sayfadan Aspose.Cells for C++'i indirin:
[İndir Aspose.Cells for C++(Linux)](https://downloads.aspose.com/cells/cpp/)
2. Paketi açın ve Linux için Aspose.Cells for C++'in nasıl kullanılacağına dair bir Demo bulacaksınız.
3. Linux komut satırınızda "cd Demo"yu çalıştırın
4. "rm -rf build;mkdir build;cd build" komutunu çalıştırın
5. "cmake .." komutunu çalıştırın, Demo klasöründe CMakeLists.txt tarafından bir Makefile oluşturacaktır.
6. Derlemek için "make" komutunu çalıştırın
 7. "./demo" komutunu çalıştırın, sonucu göreceksiniz

## **Hello World Uygulamasını Oluşturma**

Aşağıdaki adımlar, Aspose.Cells API'i kullanarak Hello World uygulamasını oluşturur:

1.  örneğini oluşturun[Çalışma kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) sınıf.
1.  Ehliyetin varsa o zaman[uygula](/cells/tr/cpp/licensing/).
 Değerlendirme sürümünü kullanıyorsanız, lisansla ilgili kod satırlarını atlayın.
1. Excel dosyasındaki bir çalışma sayfasının istediğiniz herhangi bir hücresine erişin.
1. " kelimelerini girin**Hello World!**" erişilen bir hücreye.
1. Değiştirilen Microsoft Excel dosyasını oluşturun.

Yukarıdaki adımların uygulanması aşağıdaki örneklerde gösterilmektedir.

### **Kod Örneği: Yeni Bir Çalışma Kitabı Oluşturma**

Aşağıdaki örnek, sıfırdan yeni bir çalışma kitabı oluşturur, ekler "**Hello World!**" ilk çalışma sayfasındaki A1 hücresine girer ve Excel dosyasını kaydeder.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1.cpp" >}}

### **Kod Örneği: Mevcut Bir Dosyayı Açma**

Aşağıdaki örnek, mevcut bir Microsoft Excel şablon dosyasını açar, bir hücre alır ve A1 hücresindeki değeri kontrol eder.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1.cpp" >}}
