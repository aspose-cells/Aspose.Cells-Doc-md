---
title: Yapay Zeka destekli Özellikler
type: docs
weight: 200
url: /tr/net/ai-powered-features/
keywords: Yapay Zeka, hesap tablosu, yapay zeka özellikleri, yapay zeka gücü, Excel Zeka, OpenAI, Hücreler Zeka.
description: Bu makale, elektronik tablo dosyalarını işlerken Yapay Zeka destekli özellikleri kullanmak için Adım Adım rehberdir.
---


# Yeni Kullanıcı Rehberi: Hücreler AI ile Çalışma

Hücreler AI'ye Hoşgeldiniz! Bu rehber, Hücreler AI kütüphanesini yapılandırma ve kullanma temel adımlarını anlatacaktır.

## İçindekiler
1. [Yapay Zeka Modelini Yapılandır](#configure-ai-model)
2. [Yapay Zeka Örneği Oluştur](#create-ai-instance)
3. [Dosyaları Yapay Zeka ile İşle](#process-files-with-ai)
4. [Vekil Ayarlarını Kullanma](#use-proxy-settings-if-you-can-not-access-the-ai-server-directly)

---

## Prerequisites

Before using Cells AI, ensure you have the following:
- A valid **API Key** from OpenAI or the other AI provider of your choice.
- A .NET development environment set up for C# programming.

## Configure AI Model

To start using Cells AI, you need to set up an AI model. You can either create a new model or use one of the predefined models.

### Example:
#### Setup a new AI model
```csharp
Config.Model = new Model("gpt-4-32k");
```
#### Önceden Tanımlı Yapay Zeka Modelini Kullan
```csharp
Config.Model = Model.Gpt4OMini;
```

## Yapay Zeka Örneği Oluştur

API kök URL'si ve API anahtarınızı sağlayarak HücrelerAI örneği başlatmanız gerekir. Alternatif olarak, gerekirse tam API URL'sini sağlayabilirsiniz.

### Örnek:
#### API sohbet kök URL'si ile başlatın
```csharp
String APIKey = "sk-xxxxx";
String APIRootUrl = "https://api.openai.com/";
CellsAI cellsAI = new CellsAI(APIRootUrl, APIKey);
```
#### API sohbet tam URL'si ile başlatın
```csharp
String APIKey = "sk-xxxxx";
String FullAPIRootUrl = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions";
CellsAI cellsAI = new CellsAI(FullAPIRootUrl, true, APIKey);
```

## Dosyaları Yapay Zeka ile İşle

Yapay Zeka modeli yapılandırıldıktan ve bir AI örneği oluşturulduktan sonra, elektronik tablo dosyalarını işlemek için Yapay Zeka'nın yeteneklerini kullanabilirsiniz.

### Bir Elektronik Tabloyu Özetleme::
#### Elektronik tablonun özetini alın
```csharp
// Get summary of the spreadsheet
string summary = cellsAI.SpreadsheetSummarize("c:/student.xlsx");
```

#### Ayrıca, özet çıktısını bir TextWriter'a da verebilirsiniz:
```csharp
// Use TextWriter way, Output summary to a TextWriter (Console)
TextWriter writer = Console.Out;
await cellsAI.SpreadsheetSummarize("c:/student.xlsx", writer);
```
### Bir Elektronik Tablo Üzerinde Soru Sor:
#### Elektronik tablo içeriği hakkında sorular sorabilirsiniz:
```csharp
// Ask a question about the spreadsheet
await cellsAI.SpreadsheetQuestion("c:/student.xlsx", "Who is the best student?", writer);
```
### Kullanıcı Talepleri Doğrultusunda Elektronik Tablo Oluştur:
#### Örnek:

Belirli bir talepe dayalı yeni bir elektronik tablo oluşturabilirsiniz. Örneğin, haftalık yemek planı hazırlamak gibi:
```csharp
await cellsAI.BuildSpreadsheet("Provide weekly daily three-meal recipes, including nutritional value, preparation methods, ingredients, and cost, one day per row, and add total cost at last row.", null, "c:/foodsweekly.xlsx");
```

Tarihi verilere dayanarak satış tahminleri yapabilirsiniz:

```csharp
await cellsAI.BuildSpreadsheet("Based on the sales history data from row 3 to row 10, predict the sales situation for the next year. Add it in row 11.", "c:/Sales Report Year.xlsx", "c:/Sales Report Forcast.xlsx");

```
Veya öğrenci skorlarını sıralama ile güncelleyebilirsiniz:
```csharp
await cellsAI.BuildSpreadsheet("Add a new column named \"Ranking\" and fill in the content of this column based on the students' total scores ranking", "c:\\student_score.xlsx", "c:\\student_score_with_rank.xlsx");
```
Yerelleştirilmiş Taleplerle Yapay Zeka Modeli Kullanımı:

Alibaba'nın Qianwen AI modelini veya diğer yerelleştirilmiş AI modellerini kullanabilirsiniz. İşte bir bölgeyi nasıl belirteceğiniz:
```csharp
// Set to use QwenPlus AI model
Config.Model = Model.QwenPlus;
// Set locale info (e.g., Chinese)
Config.Locale = "zh";

// User request in Chinese
string userRequest = "增加新的一列,列名称是\"排名\" 并根据学生的总分大小排名填入这一列的内容";
string outfile = "D:\\学生排行.xlsx";
string inputfile = "D:\\student_score_zh.xlsx";
await cellsAI.BuildSpreadsheet(userRequest, inputfile, outfile);

```

### Excel Formüllerini Alma:
#### Elektronik tablodan doğrudan Excel formüllerini sorgulayabilirsiniz:
```csharp
// Get formula from the spreadsheet
string formula = cellsAI.GetExcelFormula("c:/student.xlsx", "get the total score for Xiaomin");
```
## AI Sunucusuna Doğrudan Erişemiyorsanız Proxy Ayarlarını Kullanın

Bir proxy'nin arkasında çalışıyorsanız, Cells AI'nın sunucuya bağlanmasını sağlamak için proxy ayarlarını yapılandırabilirsiniz.

```csharp
// Set up proxy for Cells AI
string proxyAddress = "http://127.0.0.1:58591";
WebProxy proxy = new WebProxy(proxyAddress)
{
    BypassProxyOnLocal = false,  
    UseDefaultCredentials = false,
};

// Apply the proxy setting
cellsAI.Proxy = proxy;
```

##  Ek Özellikler ve Özelleştirmeler
Cells AI, AI modelini ayarlama, yerel ayarları belirleme ve veri çıktısını değiştirme gibi çeşitli özelleştirmelere izin verir. API'yi keşfetmek ve belirli kullanım durumunuza uygun farklı yapılandırmalarla denemeler yapmak garantilidir.

## Sonuç
Cells AI, elektronik tabloyu işleme, görevleri otomatikleştirme ve AI'den yararlanma konusunda sizi güçlendirir.  

Daha fazla bilgi için, [api dokümantasyonuna](https://reference.aspose.com/cells/net/aspose.cells.ai/) veya [destek forumuna](https://forum.aspose.com/c/cells/9) bakın.

İyi kodlamalar!
