---
title: 32 bit ve 64 bit Platformlarda Aspose.Cells kullanma
type: docs
weight: 10
url: /tr/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/
---
{{% alert color="primary" %}} 

Aspose.Cells, XCOPY dağıtımını kullanarak dağıtım sürecinizi basitleştirebilen saf bir .NET bileşenidir. Aspose.Cells'i yüklemek için bileşen grubunu (Aspose.Cells.dll) uygulamanız için bir dizine kopyalamanız yeterlidir: uygulama onu hemen kullanmaya başlayabilir. Bu, .NET bileşenlerinin kendi kendini tanımlayan doğası nedeniyle mümkündür. Bu dağıtım türünün ayrıca yükleme işlemi üzerinde sıfır etkisi vardır.

{{% /alert %}} 
## **dağıtım**
Aspose.Cells, hem 32 bit hem de 64 bit ortamları destekler. Aspose.Cells for .NET bileşenini Aspose.Cells MSI yükleyicisini kullanarak yüklediğinizde, Aspose.Cells ${installation_Path} klasör(ler)indeki farklı klasörlere farklı DLL'ler eklenir. .NET Çerçevesinin belirli bir sürümüyle kullanmanız gereken derlemeleri hangi klasörün içerdiği tablodaki açıklamaya bakın.

|**Dosya**|**Tanım**|
|:- |:- |
|net2.0|.NET Framework 2.0, 3.0, 3.5, 4.0 ve Mono ile kullanılacak derlemeleri içerir. Bunlar normalde hem 32 bit hem de 64 bit ortamlar için kullanmanız gereken derlemelerdir.|
|net2.0_AuthenticodeSigned|Yukarıdakiyle aynı, ancak derlemeler Authenticode ile dijital olarak imzalanmıştır. İmzalı derlemeler, Authenticode olmadan olduğundan daha yavaş yüklenebilir|
|net3.5_ClientProfile|.NET Framework 3.5 veya 4.0 İstemci Profili ile kullanılacak derlemeleri içerir.|
|net3.5_Müşteri profili_AuthenticodeSigned|Yukarıdakiyle aynı, ancak derlemeler Authenticode ile dijital olarak imzalanmıştır. İmzalı derlemeler, Authenticode olmadan olduğundan daha yavaş yüklenebilir.|
|net3.5|.NET Framework 3.5 veya 4.0 ile kullanılacak montajları içerir.|
|net3.5_AuthenticodeSigned|Yukarıdakiyle aynı, ancak derlemeler Authenticode ile dijital olarak imzalanmıştır. İmzalı derlemeler, Authenticode olmadan olduğundan daha yavaş yüklenebilir.|
|net4.0|.NET Framework 4.0 ve 4.5 ile kullanılacak derlemeleri içerir.|
|netStandart|.Net Standard 2.0 ile kullanılacak derlemeler içerir|
|netcoreapp2.1|.Net core 2.1 ile kullanılacak derlemeleri içerir|
|Xamarin.iOS|Xamarin. iOS ile kullanılacak derlemeler içerir|
|Xamarin.Android|Xamarin.Android ile kullanılacak derlemeleri içerir|
|net5.0|.net5.0 ile kullanılacak derlemeleri içerir.|
|net6.0|.net6.0 ile kullanılacak derlemeleri içerir.|
{{% alert color="primary" %}} 

VS.NET (örneğin 2005, 2008, 2010, 2012 vb.) projelerinde, Aspose.Cells'e referans eklerken, Referans Ekle iletişim kutusu sırasıyla net2.0 veya net3.5 klasör(ler)indeki Aspose.Cells.dll dosyalarına başvuruyor. (Daha fazla referans için, bir .NET projesinden Aspose.Cells Referansını okuyun.) Kütüphane referansını ortamınıza göre değiştirebilirsiniz. Projenin hedef çerçevesi .NET Framework 3.5/4 İstemci Profili ise, net_ClientProfile klasöründe bulunan Aspose.Cells.dll bileşen dosyasını kullanın.

{{% /alert %}}
