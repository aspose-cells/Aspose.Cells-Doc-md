---
title: Aspose.Cells Java для Ruby
type: docs
weight: 40
url: /ru/java/aspose-cells-java-for-ruby/
---

## **Введение**

### **Rjb - Ruby Java Bridge**
RJB - это мостовая программа, соединяющая Ruby и Java через Java Native Interface. Rake + Rjb - более мощный и полезный инструмент сборки, чем Maven и Ant. Вы можете протестировать свой класс бизнес-логики Java самостоятельно с помощью макета Rjb. Это помогает переносить объекты модели Struts в ваше приложение RoR. Но будьте осторожны при создании приложений Swing, Ruby (и Rjb) не учитывает обработку нативных потоков виртуальной машины Java...

### **Aspose.Cells for Java**
Aspose.Cells for Java - это награжденный компонент электронных таблиц Excel, который позволяет разработчикам Java встраивать возможность чтения, записи и манипулирования электронными таблицами Excel® (XLS, XLSX, XLSM, XLSB, XLTX, SpreadsheetML, CSV, ODS), HTML, MHTML, PDF и изображениями в их собственные Java-приложения без необходимости полагаться на Microsoft Excel®.

Aspose.Cells for Java - это зрелый, масштабируемый и функционально насыщенный компонент, который предлагает множество функций, выходящих далеко за пределы простых возможностей экспорта данных других поставщиков. С Aspose.Cells for Java разработчики могут экспортировать данные, форматировать электронные таблицы на самом мельчайшем уровне, импортировать изображения, создавать диаграммы, применять и вычислять сложные формулы, потоковые данные Excel®, сохранять в различных форматах и многое другое - все это без необходимости использования Microsoft Excel® или автоматизации Microsoft Office.
### **Aspose.Cells Java for Ruby**
Проект Aspose.Cells Java для Ruby показывает, как можно выполнять различные задачи с помощью API Aspose.Cells Java в Ruby. Этот проект призван предоставить полезные примеры для разработчиков Ruby, которые хотят использовать Aspose.Cells for Java в своих проектах Ruby с помощью Rjb (Ruby Java Bridge).
## **Требования к системе и поддерживаемые платформы**
### **Системные требования**
**Ниже приведены системные требования для использования Aspose.Cells Java для Ruby:**

- Конфигурировано Rjb Gem
- Загружен компонент Aspose.Cells
### **Поддерживаемые платформы**
**Ниже приведены поддерживаемые платформы:**

- Ruby 2.2.x или выше и соответствующий DevKit.
- Java 1.5 или выше
## **Загрузки**
### **Загрузить необходимые библиотеки**
Загрузите необходимые библиотеки, упомянутые ниже. Они необходимы для выполнения примеров Aspose.Cells Java для Ruby.

- [Компонент Aspose.Cell для Java](https://downloads.aspose.com/cells/java/)
### **Загрузить примеры из сайтов социального кодирования**
Следующие версии выполняемых примеров доступны для загрузки на указанных ниже сайтах социального кодирования:

**GitHub**

- [Aspose.Cells Java for Ruby](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **Установка и использование**
### **Установка**
Установка Aspose.cells Java для Ruby gem очень проста и легка, пожалуйста, следуйте этим простым шагам:

1. Добавьте эту строку в файл Gemfile вашего приложения. 

{{< highlight java >}}

 gem 'aspose-cellsjava'

{{< /highlight >}}

1. Затем выполните команду 

{{< highlight java >}}

 $ bundle

{{< /highlight >}}

**ИЛИ**

1. Выполните следующую команду. 

{{< highlight java >}}

 $ gem install aspose-cellsjava

{{< /highlight >}}
### **Использование**
Включите необходимые файлы для работы с примером helloworld.

{{< highlight java >}}

 require require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-cellsjava'

include Asposecellsjava

include Asposecellsjava::HelloWorld

initialize_aspose_cells

{{< /highlight >}}

Давайте разберем вышеуказанный код.

1. Первая строка убеждается в том, что aspose cells загружен и доступен.
1. Включите файлы, необходимые для доступа к aspose cells.
1. Инициализируйте библиотеки. Классы aspose JAVA загружаются из пути, указанного в файле aspose.yml/
## **Поддержка, расширение и вклад**
### **Поддержка**
С самых первых дней Aspose мы поняли, что просто предоставить нашим клиентам хорошие продукты недостаточно. Нам также необходимо предоставлять хорошее обслуживание. Мы сами являемся разработчиками и понимаем, насколько раздражающе, когда техническая проблема или особенность программного обеспечения мешает вам делать то, что вам необходимо. Мы здесь, чтобы решать проблемы, а не создавать их.

Поэтому мы предлагаем бесплатную поддержку. Каждый, кто использует наш продукт, независимо от того, купил он их или использует оценку, заслуживает нашего внимания и уважения.

Вы можете регистрировать любые проблемы или предложения, связанные с Aspose.Cells Java для Ruby, используя любые из следующих платформ:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/issues)
### **Расширение и вклад**
Aspose.Cells Java для Ruby является открытым исходным кодом, и его исходный код доступен на основных веб-сайтах для социального кодирования, перечисленных ниже. Разработчиков призывают загрузить исходный код и вносить предложения или добавлять новые функции или улучшать существующие, чтобы другие также могли извлечь пользу из этого.
### **Исходный код**
Вы можете получить последний исходный код по одному из следующих местоположений:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **Примеры кода**
**Этот раздел включает следующие темы:**

- [Загрузка и настройка Aspose.Cells в Ruby](/cells/ru/java/download-and-configure-aspose-cells-in-ruby/)
- [Руководство программиста по Ruby](/cells/ru/java/ruby-programmers-guide/)
  - [Введение в Ruby](/cells/ru/java/introduction-in-ruby/)
    - [Hello World в Ruby](/cells/ru/java/hello-world-in-ruby/)
  - [Работа с файлами в Ruby](/cells/ru/java/working-with-files-in-ruby/)
    - [Функции обработки файлов в Ruby](/cells/ru/java/file-handling-features-in-ruby/)
      - [Открытие файлов в Ruby](/cells/ru/java/opening-files-in-ruby/)
      - [Сохранение файлов в Ruby](/cells/ru/java/saving-files-in-ruby/)
    - [Утилиты в Ruby](/cells/ru/java/utility-features-in-ruby/)
      - [Преобразование диаграммы в изображение в Ruby](/cells/ru/java/converting-chart-to-image-in-ruby/)
      - [Преобразование файлов Excel в HTML в Ruby](/cells/ru/java/converting-excel-files-to-html-in-ruby/)
      - [Преобразование файлов Excel в PDF в Ruby](/cells/ru/java/converting-excel-to-pdf-files-in-ruby/)
      - [Преобразование HTML-файлов в электронные таблицы Excel в Ruby](/cells/ru/java/converting-html-files-to-excel-spreadsheets-in-ruby/)
      - [Конвертирование файлов в формате MHTML в Ruby](/cells/ru/java/converting-to-mhtml-files-in-ruby/)
      - [Конвертирование листа в изображение в Ruby](/cells/ru/java/converting-worksheet-to-image-in-ruby/)
      - [Конвертирование листа в SVG в Ruby](/cells/ru/java/converting-worksheet-to-svg-in-ruby/)
      - [Шифрование файлов Excel в Ruby](/cells/ru/java/encrypting-excel-files-in-ruby/)
      - [Управление свойствами документа в Ruby](/cells/ru/java/managing-document-properties-in-ruby/)
  - [Работа с листами в Ruby](/cells/ru/java/working-with-worksheets-in-ruby/)
    - [Отображение функций в Ruby](/cells/ru/java/display-features-in-ruby/)
      - [Показать или скрыть сетку в Ruby](/cells/ru/java/display-or-hide-gridlines-in-ruby/)
      - [Показать или скрыть заголовки строк и столбцов в Ruby](/cells/ru/java/display-or-hide-row-column-headers-in-ruby/)
      - [Показать или скрыть полосы прокрутки в Ruby](/cells/ru/java/display-or-hide-scroll-bars-in-ruby/)
      - [Показать или скрыть вкладки в Ruby](/cells/ru/java/display-or-hide-tabs-in-ruby/)
      - [Заморозить панели в Ruby](/cells/ru/java/freeze-panes-in-ruby/)
      - [Скрыть или показать лист в Ruby](/cells/ru/java/hide-or-unhide-a-worksheet-in-ruby/)
      - [Предпросмотр разбиения страниц в Ruby](/cells/ru/java/page-break-preview-in-ruby/)
      - [Разделить панели в Ruby](/cells/ru/java/split-panes-in-ruby/)
      - [Фактор масштабирования в Ruby](/cells/ru/java/zoom-factor-in-ruby/)
    - [Управление функциями в Ruby](/cells/ru/java/management-features-in-ruby/)
      - [Управление листами в Ruby](/cells/ru/java/managing-worksheets-in-ruby/)
    - [Настройка страниц в Ruby](/cells/ru/java/page-setup-features-in-ruby/)
      - [Установка параметров страницы в Ruby](/cells/ru/java/setting-page-options-in-ruby/)
    - [Функции безопасности в Ruby](/cells/ru/java/security-features-in-ruby/)
      - [Защита листов в Ruby](/cells/ru/java/protecting-worksheets-in-ruby/)
      - [Снятие защиты с листа в Ruby](/cells/ru/java/unprotect-a-worksheet-in-ruby/)
    - [Функции значения в Ruby](/cells/ru/java/value-features-in-ruby/)
      - [Копирование и перемещение листов в Ruby](/cells/ru/java/copying-and-moving-worksheets-in-ruby/)
      - [Управление разрывами страниц в Ruby](/cells/ru/java/managing-page-breaks-in-ruby/)
  - [Работа с строками и столбцами в Ruby](/cells/ru/java/working-with-rows-and-columns-in-ruby/)
    - [Настройка высоты строки и ширины столбца в Ruby](/cells/ru/java/adjusting-row-height-and-column-width-in-ruby/)
    - [Автоподгонка строк и столбцов в Ruby](/cells/ru/java/autofit-rows-and-columns-in-ruby/)
    - [Копирование строк и столбцов в Ruby](/cells/ru/java/copying-rows-and-columns-in-ruby/)
    - [Группировка и разгруппировка строк и столбцов в Ruby](/cells/ru/java/grouping-and-ungrouping-rows-and-columns-in-ruby/)
    - [Скрытие и отображение строк и столбцов в Ruby](/cells/ru/java/hiding-and-showing-rows-and-columns-in-ruby/)
    - [Вставка и удаление строк и столбцов в Ruby](/cells/ru/java/inserting-and-deleting-rows-and-columns-in-ruby/)
- [Поддержка, расширение и участие в Aspose.Cells в Ruby](/cells/ru/java/support-extend-and-contribute-to-aspose-cells-in-ruby/)
