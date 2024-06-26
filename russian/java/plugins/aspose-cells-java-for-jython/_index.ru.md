---
title: Aspose.Cells Java for Jython
type: docs
weight: 70
url: /ru/java/aspose-cells-java-for-jython/
---

## **Введение**

### **Что такое Jython?**

Jython - это Java-реализация Python, которая объединяет выразительную силу с ясностью. Jython свободно доступен как для коммерческого, так и для некоммерческого использования и поставляется с исходным кодом. Jython дополняет Java и особенно подходит для следующих задач:

- **Встраиваемый сценарий** - программисты на Java могут добавить библиотеки Jython к своей системе, чтобы позволить конечным пользователям писать простые или сложные сценарии, добавляющие функциональность к приложению.
- **Интерактивный эксперимент** - Jython предоставляет интерактивный интерпретатор, который можно использовать для взаимодействия с пакетами Java или работающими приложениями Java. Это позволяет программистам экспериментировать и отлаживать любую систему Java, используя Jython.
- **Быстрая разработка приложений** - Программы на Python обычно на 2-10 раз короче, чем эквивалентная программа на Java. Это прямо переводится в повышение производительности программиста. Беспрепятственное взаимодействие между Python и Java позволяет разработчикам свободно смешивать оба языка как во время разработки, так и в выпуске продуктов.

### **Aspose.Cells for Java**

Aspose.Cells for Java - это продвинутая библиотека классов для Java, позволяющая выполнять широкий спектр задач по обработке документов напрямую в Java
приложениях.

Aspose.Cells for Java поддерживает обработку ячеек (DOC, DOCX, OOXML, RTF) HTML, OpenDocument, PDF, EPUB, XPS, SWF и все форматы изображений. С помощью Aspose.Cells вы можете
создавать, изменять и преобразовывать документы, не используя пакет Microsoft Office.

### **Aspose.Cells Java for Jython**

Aspose.Cells Java для Jython - это проект, демонстрирующий / предоставляющий примеры использования API Aspose.Cells for Java на Jython.

## **Требования к системе и поддерживаемые платформы**

### **Системные требования**

**Следующие системные требования для использования Aspose.Cells Java для Jython:**

- Java 1.5 или выше установлен
- Загружен компонент Aspose.Cells
- Jython 2.7.0

### **Поддерживаемые платформы**

**Ниже приведены поддерживаемые платформы:**

- Aspose.Cells 15.4 и выше.
- Среда разработки Java (Eclipse, NetBeans ...)

## **Загрузить установку и использование**

### **Загрузка**

**Загрузить примеры с веб-сайтов для социального программирования**

Ниже приведены релизы запущенных примеров, доступные для скачивания на всех указанных ниже сайтах социального кодирования:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)

**Загрузить компонент Aspose.Cells for Java**

- [Aspose.Cells for Java](https://releases.aspose.com/cells/java/)

### **Установка**

- Поместите загруженный файл Aspose.Cells for Java jar в каталог "lib".
- Замените "your-lib" на имя загруженного jar файла в файле _*init*_.py.

### **Использование**

Вы можете создать документ HelloWorld, используя следующий пример кода:

{{< highlight java >}}

 from aspose-cells  import Settings

from com.aspose.Cells import Document

from com.aspose.Cells import DocumentBuilder

class HelloWorld:

    def __init__(self):

        dataDir = Settings.dataDir + 'quickstart/'



        workbook = Workbook()



        sheet = workbook.getWorksheets().get(0)



        cell = sheet.getCells().get("A1")



        cell.setValue("Hello World!")



        file_format_type = FileFormatType



        workbook.save(dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )



        print "Document has been saved, please check the output file.";

if __name__ == '__main__':

    HelloWorld()

{{< /highlight >}}

## **Поддержка, расширение и вклад**

### **Поддержка**

С самых первых дней Aspose мы поняли, что просто предоставить нашим клиентам хорошие продукты недостаточно. Нам также необходимо предоставлять хорошее обслуживание. Мы сами являемся разработчиками и понимаем, насколько раздражающе, когда техническая проблема или особенность программного обеспечения мешает вам делать то, что вам необходимо. Мы здесь, чтобы решать проблемы, а не создавать их.

Поэтому мы предлагаем бесплатную поддержку. Каждый, кто использует наш продукт, независимо от того, купил он их или использует оценку, заслуживает нашего внимания и уважения.

Вы можете зарегистрировать любые проблемы или предложения, связанные с Aspose.Cells Java для Jython, в одной из следующих платформ:

- [Github](https://github.com/aspose-words/Aspose.Words-for-Java/issues)

### **Расширение и вклад**

Aspose.Cells Java для Jython является открытым исходным кодом, и его исходный код доступен на основных сайтах для совместной разработки, перечисленных ниже. Разработчиков призывают загружать исходный код и вносить свой вклад, предлагая или добавляя новые функции или улучшая существующие, чтобы другие тоже могли извлечь из этого пользу.

### **Исходный код**

Вы можете получить последний исходный код в одном из следующих мест

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)
