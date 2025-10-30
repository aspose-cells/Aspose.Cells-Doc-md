---
title: Aspose.Cells i 32 bit ve 64 bit Platformlarda Kullanma
type: docs
weight: 10
url: /tr/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/
---

{{% alert color="primary" %}} 

Aspose.Cells, XCOPY dağıtımını kullanarak dağıtım sürecinizi basitleştirebilen saf .NET bileşenidir. Aspose.Cells'i yüklemek için, bileşen derlemesini (Aspose.Cells.dll) uygulamanız için bir dizine kopyalayabilirsiniz: uygulama hemen kullanmaya başlayabilir. Bu, .NET bileşenlerinin kendi kendini tanımlayan doğası sayesinde mümkündür. Bu tür bir dağıtımın kurulum süreci üzerinde de sıfır etkisi vardır.

{{% /alert %}} 
## **Dağıtım**
Aspose.Cells, hem 32-bit hem de 64-bit ortamları destekler. Aspose.Cells MSI yükleyicisini kullanarak Aspose.Cells for .NET bileşenini yüklediğinizde, farklı .NET Framework sürümleriyle kullanmanız gereken yapıları farklı klasörlere ekler. Hangi klasörün hangi .NET Framework sürümüyle kullanılması gereken yapıları içerdiği tablodaki açıklamaya bakınız.

|**Klasör**|**Açıklama**|
| :- | :- |
|net2.0|.NET Framework 2.0, 3.0, 3.5, 4.0 ve Mono ile kullanılacak derlemeleri içerir. Bunlar, genellikle hem 32-bit hem de 64-bit ortamlar için normalde kullanmanız gereken derlemelerdir.|
|net2.0_AuthenticodeSigned|Yukarıdakiyle aynı, ancak derlemeler Authenticode ile dijital olarak imzalanmıştır. İmzalı derlemeler, Authenticode olmadan olanlardan daha yavaş yüklenir.|
|net3.5_ClientProfile|.NET Framework 3.5 veya 4.0 Client Profile ile kullanılacak derlemeleri içerir.|
|net3.5_ClientProfile_AuthenticodeSigned|Yukarıdakiyle aynı, ancak derlemeler Authenticode ile dijital olarak imzalanmıştır. İmzalı derlemeler, Authenticode olmadan olanlardan daha yavaş yüklenir.|
|net3.5|.NET Framework 3.5 veya 4.0 ile kullanılacak derlemeleri içerir.|
|net3.5_AuthenticodeSigned|Yukarıdakiyle aynı, ancak derlemeler Authenticode ile dijital olarak imzalanmıştır. İmzalı derlemeler, Authenticode olmadan olanlardan daha yavaş yüklenir.|
|net4.0|.NET Framework 4.0 ve 4.5 ile kullanılacak derlemeleri içerir.|
|netStandard|.Net Standard 2.0 ile kullanılacak derlemeleri içerir|
|netcoreapp2.1|.Net core 2.1 ile kullanılacak derlemeleri içerir|
|Xamarin.iOS|Xamarin.iOS ile kullanılacak derlemeleri içerir|
|Xamarin.Android|Xamarin.Android ile kullanılacak derlemeleri içerir|
|net5.0|.net5.0 ile kullanılacak derlemeleri içerir|
|net6.0|.net6.0 ile kullanılacak derlemeleri içerir|
|net8.0|.net8.0 ile kullanmak için derlemeleri içerir.|
|net9.0|.net9.0 ile kullanmak için derlemeleri içerir.|

{{% alert color="primary" %}} 

VS.NET'de (örneğin 2005, 2008, 2010, 2012 vb.) projelere Aspose.Cells'e bir referans eklediğinizde, Aspose.Cells.dll dosyalarına sırasıyla net2.0 veya net3.5 klasör(ler)indeki Add Reference iletişim kutusu söz konusudur. (Daha fazla bilgi için .NET projesinden Aspose.Cells'e atıfta bulunma bölümünü okuyun.) Referansı ortamınıza göre kütüphaneye değiştirebilirsiniz. Lütfen projenin hedef çerçevesini .NET Framework 3.5/4 Client Profile ise, net_ClientProfile klasöründe bulunan Aspose.Cells.dll bileşen dosyasını kullanın.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
