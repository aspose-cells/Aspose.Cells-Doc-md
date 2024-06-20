---
title: Начало работы
type: docs
weight: 10
url: /ru/net/getting-started/
---

{{% alert color="primary" %}} 

На этой странице вы узнаете, как установить Aspose Cells и создать приложение Hello World.

{{% /alert %}}

## **Установка**

### **Установите Aspose.Cells через NuGet**

NuGet - самый простой способ скачать и установить Aspose.Cells for .NET. 

1. Откройте Microsoft Visual Studio и менеджер пакетов NuGet. 
1. Введите "aspose.cells", чтобы найти нужный Aspose.Cells for .NET. 
1. Нажмите "Установить", Aspose.Cells for .NET будет загружен и добавлен в ваш проект.
**![Установить Aspose.Cells через NuGet](install-through-nuget.png)**

Вы также можете загрузить его со страницы NuGet для aspose.cells: 
[Пакет NuGet Aspose.Cells for .NET](https://www.nuget.org/packages/Aspose.Cells/)

[Дополнительные шаги для подробностей](/cells/ru/net/installation/)

### **Установите Aspose.Cells на windows**

1. Скачайте Aspose.Cells.msi из следующей страницы:
[Скачать Aspose.Cells.msi](https://downloads.aspose.com/cells/net/)
1. Дважды щелкните Aspose Cells msi и следуйте инструкциям по установке:

**![Установить Aspose Cells на windows](install-on-windows.png)**

[Дополнительные шаги для подробностей](/cells/ru/net/installing-aspose-cells-on-windows/)

### **Установите Aspose.Cells в Linux**

В этом примере я использую Ubuntu, чтобы показать, как начать использовать Aspose.Cells в Linux.

1. Создайте приложение .netcore с именем "AsposeCellsTest".
2. Откройте файл "AsposeCellsTest.csproj", добавьте в него следующие строки для ссылок на пакет Aspose.Cells:
{{< highlight plain >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="24.6" />
  </ItemGroup>
{{< /highlight >}}
3. Откройте проект в VSCode на Ubuntu:
**![Установка Aspose Cells на linux](install-on-linux.png)**
4. запустите тест с помощью следующего кода:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

Примечание: Aspose.Cells для .NetStandard может поддерживать вашу потребность в linux.

Применяется к: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 и более новые версии.

### **Установка Aspose.Cells на MAC OS**

В этом примере я использую macOS High Sierra, чтобы показать, как начать использовать Aspose.Cells на MAC OS.

1. Создайте приложение .netcore с именем "AsposeCellsTest".
2. Откройте приложение в Visual Studio для Mac, затем установите Aspose Cells через NuGet:
**![Установка Aspose Cells на macOS](install-on-mac-os.png)**
3. запустите тест с помощью следующего кода:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4. Если вам нужно использовать функции, связанные с рисованием, установите libgdiplus в macOS, см .:
[Как установить libgdiplus в macOS](/cells/ru/net/how-to-install-libgdiplus-in-macos/)

Примечание: Aspose.Cells для .NetStandard может поддерживать вашу потребность на MAC OS.

Применяется к: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 и более новые версии.

### [**Run Aspose Cells in Docker**](/cells/ru/net/how-to-run-aspose-cells-in-docker/)

### **Как использовать графическую библиотеку на платформах non-windows с Net6**

Aspose.Cells для Net6 теперь использует SkiaSharp в качестве графической библиотеки, как рекомендовано в [официальном заявлении Microsoft](https://github.com/dotnet/designs/blob/f9d006073b7a019bd2021e99c66516447f7fb1a6/accepted/2021/system-drawing-win-only/system-drawing-win-only.md). Для получения более подробной информации о использовании Aspose.Cells с NET6, см. [Как запустить Aspose.Cells для .Net6](/cells/ru/net/how-to-run-aspose-cells-for-net6/).

## **Создание приложения Hello World**

Нижеприведенные шаги создают приложение Hello World с использованием API Aspose.Cells:

1. Если у вас есть лицензия, то [примените ее](/cells/ru/net/licensing/).
   Если вы используете пробную версию, пропустите строки кода, связанные с лицензией.
1. Создайте экземпляр класса [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook), чтобы создать новый файл Excel или открыть существующий файл Excel.
1. Получите доступ к любой желаемой ячейке листа Excel в файле Excel.
1. Вставьте слова **Привет, мир!** в ячейку для доступа.
1. Сгенерируйте модифицированный файл Microsoft Excel.

Реализация вышеуказанных шагов продемонстрирована в примерах ниже.

### **Пример кода: Создание новой книги**

В следующем примере создается новая книга из ничего, вставляется "Hello World!" в ячейку A1 на первом рабочем листе и сохраняется как файл Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **Пример кода: Открытие существующего файла**

В следующем примере открывается существующий файл шаблона Microsoft Excel "Sample.xlsx", вставляется "Hello World!" в ячейку A1 на первом рабочем листе и сохраняется как файл Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
