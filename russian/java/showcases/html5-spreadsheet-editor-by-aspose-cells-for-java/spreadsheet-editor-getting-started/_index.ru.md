---
title: Начало работы с редактором таблиц
type: docs
weight: 10
url: /ru/java/spreadsheet-editor-getting-started/
---

**Содержание**

- [Введение](#SpreadsheetEditorGettingStarted-Introduction)
- [Системные требования](#SpreadsheetEditorGettingStarted-SystemRequirements)
- [Загрузка и установка](#SpreadsheetEditorGettingStarted-DownloadandInstallation)
- [Поддержка](#SpreadsheetEditorGettingStarted-Support)
- [Внести вклад](#SpreadsheetEditorGettingStarted-Contribute)
- [Лицензия](#SpreadsheetEditorGettingStarted-License)
### **Введение**
Html5 Spreadsheet Editor - веб-приложение, которое позволяет просматривать и редактировать электронные таблицы в веб-браузере. Оно поддерживает Excel, SpreadsheetML, CVS, OpenDocument и многие другие форматы, поддерживаемые Microsoft Excel. Поддерживаются все основные функции, включая редактирование ячеек, форматирование, редактирование формул, управление строками и столбцами и т. д.

![todo:image_alt_text](aowcrc1.png)

Редактор электронных таблиц HTML5 использует множество функций [Aspose.Cells for Java](https://products.aspose.com/cells/java/) и показывает, как их использовать для создания, изменения и отображения электронной таблицы в вашем приложении на Java.

**Особенности**

- Работа с файлами 
  - Поддерживаемые форматы
  - Открыть локальные файлы
  - Открыть из Dropbox
  - Открыть по URL
  - Создать новую электронную таблицу
  - Экспорт в различные форматы
- Работа с листами 
  - Добавление и удаление листов
  - Переименование листов
  - Переключение между листами
- Работа с строками и столбцами 
  - Добавить строку
  - Добавить столбец
  - Удалить строку
  - Удалить столбец
  - Ширина столбца и высота строки
- Работа с ячейками 
  - Выбор ячейки
  - Редактирование ячейки
  - Редактирование формулы
  - Выравнивание ячейки
  - Очистить ячейку
  - Добавить ячейку
  - Удалить ячейку
- Работа с форматированием текста 
  - Жирный, курсив, подчеркнутый
  - Стиль и размер шрифта
  - Очистить форматирование
### **Системные требования**
**Требования к программному обеспечению**

- Поддерживаемый Java-сервер приложений CDI
- [Aspose.Cells for Java](https://products.aspose.com/cells/java/)
- [JavaServer Faces 2.0](https://javaee.github.io/javaserverfaces-spec/)
- [Primefaces 5.1](https://www.primefaces.org/)

**Требования к аппаратному обеспечению**

Требования к аппаратному обеспечению могут варьироваться в зависимости от выбора сервера приложений Java, на котором мы планируем развернуть редактор электронных таблиц HTML5 и количества электронных таблиц, которые мы открываем одновременно. Ниже приведена оценка, которая поможет настроить среду в начальной стадии.

- 2 GHz CPU
- 2 GB RAM
- 500 МБ дискового пространства
### **Загрузка и установка**
Редактор электронных таблиц HTML5 - это приложение Java EE и может быть развернуто на любом сервере приложений Java с поддержкой CDI. Он был протестирован с [Glassfish](https://javaee.github.io/glassfish/).

**Исходный код**

Исходный код проекта доступен на [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/). Мы также ведем зеркала Git на следующих сайтах:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [Google Code](https://code.google.com/archive/p/html5-spreadsheet-editor/)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

Используйте одну из следующих команд для загрузки исходного кода через командную строку:

**Github**

{{< highlight bash >}}

 git clone https://github.com/aspose-cells/Aspose.Cells-for-Java.git

{{< /highlight >}}

**Bitbucket**

{{< highlight bash >}}

 git clone https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java.git

{{< /highlight >}}

**Google Code**

{{< highlight bash >}}

 git clone https://code.google.com/p/html5-spreadsheet-editor/

{{< /highlight >}}

**SourceForge**

{{< highlight bash >}}

 git clone git://git.code.sf.net/p/html5-spreadsheet-editor/code html5-spreadsheet-editor-code

{{< /highlight >}}

**Сборка с использованием Maven**

Процесс сборки проекта управляется с помощью Maven. Таким образом, вы можете подготовить WAR-файл из командной строки без использования IDE. Используйте следующую команду для создания WAR-файла для развертывания. Документация соответствующего сервера приложений поможет вам развернуть сгенерированный WAR и его зависимости.

{{< highlight java >}}

 mvn clean install

{{< /highlight >}}

**Использование NetBeans**

Очень легко управлять проектом с использованием [NetBeans IDE](https://netbeans.apache.org/). NetBeans - одна из популярных ИТС среди разработчиков на Java и спонсируется Oracle.

- Загрузите исходный код проекта.
- Откройте проект в среде NetBeans IDE.
- Нажмите кнопку ***Запустить*** на панели инструментов.
- Выберите сервер ***Glassfish*** в качестве сервера приложений.

**Использование Eclipse**

[Среда разработки Eclipse IDE](http://www.eclipse.org/ide/) предоставляет официальную интеграцию для импорта проектов Maven, называемую [M2Eclipse](http://www.eclipse.org/m2e/):

1. Установите M2Eclipse в своей среде разработки Eclipse IDE. Процедура установки описана на их веб-сайте.
1. Загрузите исходный код проекта.
1. Откройте ***Диалог импорта*** в меню Файл.
1. Выберите ***Maven Project*** из диалога импорта.
1. Нажмите ***Далее***.
1. Нажмите ***Обзор***, чтобы выбрать местоположение исходного кода.
1. Выберите ***pom.xml*** из списка ниже.
1. Нажмите ***Готово***.

Среда разработки Eclipse IDE должна импортировать и загрузить проект.
### **Поддержка**
**Отчет об ошибке**

Чтобы отправить отчет об ошибке, создайте новую проблему на [странице проекта Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) и примените метку ***bug***.

**Запрос на добавление функции**

Мы высоко ценим ваш отзыв и предложения по функционалу. Чтобы запросить новую функцию или улучшение существующей, создайте новый вопрос на [странице проекта Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) и добавьте метку ***enhancement***.

**Вопросы и помощь**

Вы можете задать любые вопросы, связанные с редактором таблиц HTML5, используя [вопрос на Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues). Просто создайте новый вопрос и добавьте метку ***question***.

**Форумы Aspose.Cells for Java**

Форумы продукта Aspose предоставляют полную поддержку как для пробных, так и для платных клиентов. Эксперты работают 24/7, чтобы помочь и ответить на вопросы. Посетите [форумы продукта здесь](https://forum.aspose.com/c/cells/9).

**Блоги Aspose**

Будьте на связи с нами и будьте в курсе последних новостей о наших продуктах и предложениях. Подпишитесь на [наш блог здесь](http://blog.aspose.com).
### **Внести вклад**
[](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)

[!\[todo:image_alt_text\](https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png)](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)


Редактор таблиц HTML5 - это проект с открытым исходным кодом, который позволяет максимальные возможности для всех внести свой вклад в проект.

**Исходный код**

Исходный код проекта доступен на [Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java). Мы также ведем Git-зеркала на следующих сайтах:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

**Запросы на вытягивание (Pull Requests)**

Для внесения изменений в исходный код проекта отправьте запрос на вытягивание через Github. Получите больше информации в статье Github о [Создании запроса на вытягивание](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).
### **Лицензия**
**Лицензия MIT**

Мы используем одну из наиболее либеральных лицензий с открытым исходным кодом для минимальной ответственности участников. Редактор таблиц HTML5 выпущен под [лицензией MIT](https://opensource.org/licenses/mit-license.php).

**Лицензия Aspose**

Продукт работает без лицензии Aspose, [с ограничениями](/cells/ru/java/licensing/). Чтобы убрать ограничения, вы можете получить [бесплатную временную лицензию](https://purchase.aspose.com/temporary-license) или [купить полную лицензию](https://purchase.aspose.com/buy).

По умолчанию редактор будет пытаться загрузить файл **Aspose.Total.Java.lic** из каталога **src/main/resources/com/aspose/spreadsheeteditor**. Просто скопируйте файл лицензии в этот каталог. Поведение по умолчанию можно изменить, отредактировав класс **AsposeLicense**.
