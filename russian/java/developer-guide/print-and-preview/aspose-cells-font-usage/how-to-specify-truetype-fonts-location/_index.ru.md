---
title: Как указать местоположение шрифтов TrueType
type: docs
weight: 30
url: /ru/java/how-to-specify-truetype-fonts-location/
---

{{% alert color="primary" %}}

В этой статье описано:

1. [Где API Aspose.Cells ищет шрифты TrueType](/cells/ru/java/how-to-specify-truetype-fonts-location/#where-asposecells-looks-for-truetype-fonts-on-windows).
1. [Как явно указать папки TrueType шрифтов для API Aspose.Cells](/cells/ru/java/how-to-specify-truetype-fonts-location/#how-to-explicitly-specify-a-font-folder).
1. [Как ограничить использование API Aspose.Cells только одним местоположением шрифтов TrueType](/cells/ru/java/how-to-specify-truetype-fonts-location/#how-to-restrict-the-asposecells-to-use-only-one-font-folder).

{{% /alert %}}

## **Работа с шрифтами**

### **Где Aspose.Cells ищет шрифты TrueType в Windows**

Aspose.Cells ищет шрифты в папке **Windows\Fonts**. Это настройка по умолчанию, которая работает большую часть времени, поэтому указывайте свои собственные папки со шрифтами, только если вам действительно это нужно.

### **Где Aspose.Cells ищет шрифты TrueType в Linux**

По умолчанию API Aspose.Cells ищет шрифты во всех следующих местах, хотя различные дистрибутивы Linux хранят шрифты в разных папках.

1. /usr/share/fonts
1. /usr/local/share/fonts

{{% alert color="primary" %}}

Это поведение по умолчанию будет работать для большинства дистрибутивов Linux, но не гарантируется, что будет работать всегда. Вам может потребоваться явно указать местоположение шрифтов TrueType. 

{{% /alert %}}

### **Как явно указать папку со шрифтами**

API Aspose.Cells предоставляет множество методов для класса FontConfigs для указания шрифтов или папок со шрифтами, как описано ниже.

1. Метод setFontFolder принимает первым параметром строку с местоположением каталога шрифтов, в то время как второй параметр типа Boolean направляет Aspose.Cells APis на поиск файлов шрифтов в папках рекурсивно.
1. Метод setFontFolders принимает массив строк, поэтому вы можете указать множество каталогов шрифтов с помощью этого подхода. Вы также можете направить Aspose.Cells APis на рекурсивный поиск файлов шрифтов, указав true вторым параметром.
1. Метод setFontSources принимает массив типа FontSourceBase, чтобы вы могли указать список местоположений отдельных шрифтов.

{{% alert color="primary" %}}

При указании папки со шрифтами с использованием любого из вышеупомянутых методов мы рекомендуем установить местоположение шрифта в начале приложения, иначе вы можете получить плохо отформатированные результаты.

{{% /alert %}} {{% alert color="primary" %}}

Установка папки со шрифтами с использованием любого из вышеперечисленных методов не гарантирует, что API Aspose.Cells не будет искать шрифты в папках по умолчанию, таких как системная папка шрифтов.

{{% /alert %}}

### **Как ограничить Aspose.Cells использовать только одну папку со шрифтами**

Начиная с Aspose.Cells for Java 8.1.0, установка аргументов JVM в виде **-DAspose.Cells.FontDirExc="YourFontDir** гарантирует, что API Aspose.Cells будет использовать только указанное местоположение шрифтов.

Установите указанные аргументы, используя метод System.setProperty, как показано ниже.

{{< highlight java >}}

System.setProperty("Aspose.Cells.FontDirExc", "FontDirSet");

{{< /highlight >}}

{{% alert color="primary" %}}

Обратите внимание на следующее:

- Указанное выше утверждение должно быть в начале вашего приложения.
- Использование вышеперечисленного подхода не требует установки папки со шрифтами с использованием любого из методов FontConfigs, обсужденных выше.
- Строка "FontDirSet" должна представлять собой полный путь к папке, содержащей необходимые шрифты.

{{% /alert %}}
