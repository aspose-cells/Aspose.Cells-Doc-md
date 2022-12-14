---
title: Начало работы с редактором электронных таблиц
type: docs
weight: 10
url: /ru/java/spreadsheet-editor-getting-started/
---
**Оглавление**

- [Введение](#SpreadsheetEditorGettingStarted-Introduction)
- [Системные Требования](#SpreadsheetEditorGettingStarted-SystemRequirements)
- [Загрузка и установка](#SpreadsheetEditorGettingStarted-DownloadandInstallation)
- [Поддерживать](#SpreadsheetEditorGettingStarted-Support)
- [Делать вклад](#SpreadsheetEditorGettingStarted-Contribute)
- [Лицензия](#SpreadsheetEditorGettingStarted-License)
### **Введение**
Редактор электронных таблиц Html5 — это веб-приложение, которое может просматривать и редактировать электронные таблицы в веб-браузере. Он поддерживает Excel, SpreadsheetML, CVS, OpenDocument и многие другие форматы, поддерживаемые Microsoft Excel. Поддерживаются все основные функции, включая редактирование ячеек, форматирование, редактирование формул, управление строками и столбцами и т. д.

![дело:изображение_альтернативный_текст](aowcrc1.png)

 Редактор электронных таблиц HTML5 использует многие функции[Aspose.Cells for Java](https://products.aspose.com/cells/java/)и показывает, как использовать их для создания, обработки и визуализации электронных таблиц в вашем приложении Java.

**Функции**

-  Работа с файлами
 - Поддерживаемые форматы
 - Открыть локальные файлы
 - Открыть из Dropbox
 - Открыть с URL-адреса
 - Создать новую таблицу
 - Экспорт в различные форматы
-  Работа с листами
 - Добавить и удалить листы
 - Переименовать листы
 - Переключение между листами
-  Работа со строками и столбцами
 - Добавить строку
 - Добавить столбец
 - Удалить строку
 - Удалить столбец
 - Ширина столбца и высота строки
-  Работа с Cells
 - Выбор ячейки
 - Редактирование ячейки
 - Формула редактирования
 - Cell развал
 - Очистить Cell
 - Добавить ячейку
 - Удалить ячейку
-  Работа с форматированием текста.
 - Жирный, курсив, подчеркивание
 - Стиль и размер шрифта
 - Очистить форматирование
### **Системные Требования**
**Требования к программному обеспечению**

- CDI поддерживает сервер приложений Java
- [Aspose.Cells for Java](https://products.aspose.com/cells/java/)
- [JavaServer Faces 2.0](https://javaee.github.io/javaserverfaces-spec/)
- [Перволики 5.1](https://www.primefaces.org/)

**Требования к оборудованию**

Требования к оборудованию различаются в зависимости от сервера приложений Java, который мы выбираем для развертывания редактора электронных таблиц HTML5, и количества электронных таблиц, которые мы открываем одновременно. Ниже приведена оценка, которая поможет первоначально настроить среду.

- ЦП 2 ГГц
- 2 ГБ оперативной памяти
- Диск 500 МБ
### **Загрузка и установка**
 Редактор электронных таблиц HTML5 — это приложение Java EE, которое можно развернуть в любом веб-профиле сервера приложений Java с поддержкой CDI. Он был протестирован с[Стеклянная рыба](https://javaee.github.io/glassfish/).

**Исходный код**

 Исходный код проекта доступен по адресу[Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/). Мы также поддерживаем зеркала Git на следующих сайтах:

- [Битбакет](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [Google Код](https://code.google.com/archive/p/html5-spreadsheet-editor/)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

Используйте одну из следующих команд для загрузки исходного кода через командную строку:

**Гитхаб**

{{< highlight "bash" >}}

 git clone https://github.com/aspose-cells/Aspose.Cells-for-Java.git

{{< /highlight >}}

**Битбакет**

{{< highlight "bash" >}}

 git clone https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java.git

{{< /highlight >}}

**Google Код**

{{< highlight "bash" >}}

 git clone https://code.google.com/p/html5-spreadsheet-editor/

{{< /highlight >}}

**SourceForge**

{{< highlight "bash" >}}

 git clone git://git.code.sf.net/p/html5-spreadsheet-editor/code html5-spreadsheet-editor-code

{{< /highlight >}}

**Сборка с использованием Maven**

Процесс сборки проекта управляется с помощью Maven. Таким образом, вы можете подготовить файл WAR из командной строки без какой-либо IDE. Используйте следующую команду, чтобы создать WAR для развертывания. Документация соответствующего сервера приложений поможет вам развернуть сгенерированный файл WAR и его зависимости.

{{< highlight "java" >}}

 mvn clean install

{{< /highlight >}}

**Использование NetBeans**

 Очень легко управлять проектом с помощью[IDE NetBeans](https://netbeans.apache.org/). NetBeans — одна из популярных IDE среди Java разработчиков, спонсируемая Oracle.

- Загрузите исходный код проекта.
- Откройте проект в среде IDE NetBeans.
-  Нажмите***Бежать*** кнопка на панели инструментов.
-  Выбирать***Стеклянная рыба*** сервер в качестве сервера приложений.

**Использование затмения**

[Затмение IDE](http://www.eclipse.org/ide/) обеспечивает официальную интеграцию для импорта Maven проектов под названием[M2Затмение](http://www.eclipse.org/m2e/):

1. Установите M2Eclipse в Eclipse IDE. Процедура установки описана на их сайте.
1. Загрузите исходный код проекта.
1. Открой***импорт*** диалоговое окно из меню «Файл».
1.  Выбирать***Maven Проект*** из диалогового окна импорта.
1.  Нажмите***Следующий***.
1.  Нажмите***Просматривать*** для выбора местоположения исходного кода.
1.  Выбирать***пом.xml*** из списка ниже.
1.  Нажмите***Заканчивать***.

Eclipse IDE должна импортировать и загрузить проект.
### **Поддерживать**
**Отчет об ошибке**

 Чтобы отправить отчет об ошибке, создайте новую задачу на[Страница проекта на гитхабе](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) и применить метку***ошибка***.

**Запрос функции**

 Мы высоко ценим ваши отзывы и функции, которые вы запрашиваете. Чтобы запросить новую функцию или улучшение существующей, создайте новую проблему на[Страница проекта на гитхабе](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) и применить метку***улучшение***.

**Вопросы и помощь**

 Вы можете задать любой вопрос, связанный с редактором электронных таблиц HTML5, используя[проблема с гитхабом](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) . Просто создайте новую задачу и примените***вопрос*** этикетка.

**Aspose.Cells for Java Форумы**

 Aspose форумы по продуктам обеспечивают полную поддержку как для пробных, так и для платных клиентов. Эксперты работают круглосуточно и без выходных, чтобы помочь и ответить на вопросы. Посещать[форумы по продуктам здесь](https://forum.aspose.com/c/cells/9).

**Aspose Блоги**

 Свяжитесь с нами и будьте в курсе последних новостей о наших продуктах и предложениях. Подписаться на[наш блог здесь](http://blog.aspose.com).
### **Делать вклад**
[](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)

[!\[задача:image_alt_text\]](https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png)](https://github.com/AsposeShowcase/Html5_Электронная таблица_редактор_по_Aspose.Cells_за_Java)


Редактор электронных таблиц HTML5 — это проект с открытым исходным кодом, который позволяет каждому внести свой вклад в проект.

**Исходный код**

 Исходный код проекта доступен по адресу[Гитхаб](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java). Мы также поддерживаем зеркала Git на следующих сайтах:

- [Битбакет](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

**Пулл-реквесты**

 Чтобы внести исходный код в проект, просто отправьте запрос на извлечение через Github. Подробнее читайте в статье Github о[Создать запрос на вытягивание](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).
### **Лицензия**
**Лицензия Массачусетского технологического института**

 Мы используем одну из самых либеральных лицензий с открытым исходным кодом для минимальных обязательств перед участниками. Редактор электронных таблиц HTML5 выпущен под[Лицензия Массачусетского технологического института](https://opensource.org/licenses/mit-license.php).

**Aspose Лицензия**

 Продукт работает без лицензии Aspose,[с ограничениями](/cells/ru/java/licensing/) . Чтобы снять ограничения, вы можете приобрести[бесплатная временная лицензия](https://purchase.aspose.com/temporary-license) или же[купить полную лицензию](https://purchase.aspose.com/buy).

 По умолчанию редактор попытается загрузить**Aspose.Total.Java.lic** файл из**src/main/resources/com/aspose/spreadsheeteditor** каталог. Просто скопируйте файл лицензии в этот каталог. Поведение по умолчанию можно изменить, отредактировав**AsposeЛицензия** учебный класс.
