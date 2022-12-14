---
title: Başlarken
type: docs
weight: 10
url: /tr/cpp/getting-started/
description: C++ için Aspose Cells nasıl kurulur ve Hello World uygulaması nasıl oluşturulur.
---
{{% alert color="primary" %}} 

Bu sayfa, C++ için Aspose Cells'i nasıl kuracağınızı ve Hello World uygulamasını nasıl oluşturacağınızı gösterecektir.

{{% /alert %}}

## **Kurulum**

### **Aspose Cells ila NuGet'i yükleyin**

 NuGet, C++ için Aspose.Cells'i indirip kurmanın en kolay yoludur.
1. C++ için bir Microsoft Visual Studio projesi oluşturun.
2. "Aspose.Cells.h" başlık dosyasını ekleyin.
3. Microsoft Visual Studio ve NuGet paket yöneticisini açın.
 4. C++ için istenen Aspose.Cells'i bulmak için "aspose.cells.cpp" araması yapın.
5. "Yükle"ye tıklayın, C++ için Aspose.Cells indirilecek ve projenizde referans gösterilecektir.

**![Aspose Cells ila NuGet'i yükleyin](InstallThroughNuget.png)**

 aspose.cells için nuget web sayfasından da indirebilirsiniz:
[C++ NuGet Paketi için Aspose.Cells](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[Ayrıntılar için daha fazla adım](/cells/tr/cpp/installation/)

### **Windows'de C++ için Aspose.Cells'i kullanmak için bir demo**

1. Aşağıdaki sayfadan C++ için Aspose.Cells'i indirin:
[C++(Windows) için Aspose.Cells'i indirin](https://downloads.aspose.com/cells/cpp/)
2. Paketi açın ve C++ için Aspose.Cells'in nasıl kullanılacağına dair bir Demo bulacaksınız.
3. Demo.sln dosyasını Visual Studio 2017 veya daha yüksek sürümle açın
4. main.cpp: bu dosya Aspose.Cells'in C++ için nasıl test edileceğini gösterir.
 5. sourceFile/resultFile: bu iki klasör main.cpp'de kullanılan depolama dizinleridir.

### **Linux işletim sisteminde C++ için Aspose.Cells nasıl kullanılır?**

1. Aşağıdaki sayfadan C++ için Aspose.Cells'i indirin:
[C++(Linux) için Aspose.Cells'i indirin](https://downloads.aspose.com/cells/cpp/)
2. Paketi açın ve Linux için C++ için Aspose.Cells'in nasıl kullanılacağı hakkında bir Demo bulacaksınız.
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
