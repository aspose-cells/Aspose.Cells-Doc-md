---
title: Введение в GridWeb
type: docs
weight: 10
url: /ru/java/introduction-of-gridweb/
---
## **Основы GridWeb**
Aspose.Cells.GridWeb - это веб-контроллер с графическим интерфейсом, который можно встраивать в веб-страницы JSP или любую html-страницу в Java-сервере. 
 

Он легкий и прост в использовании.

Он помогает вам быстро создать онлайн-редактор электронных таблиц для файлов электронных таблиц.

Он также поддерживает импорт и экспорт всех видов файлов электронных таблиц, которые на 100% совместимы с файлами MS Excel.

## **Aspose.Cells.GridWeb - Демонстрации**
 

Для быстрого старта мы предоставляем несколько примеров кода и демонстраций, показывающих, как использовать API Aspose.Cells.GridWeb.

Пожалуйста, загрузите демонстрации по следующей ссылке:
[Демонстрации Aspose.Cells.GridWeb](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)


## **Как запустить демонстрации Aspose.Cells для GridWeb на Java**
{{% alert color="primary" %}} 

Демонстрации Aspose.Cells для GridWeb на Java легко запустить. Вам просто нужно развернуть **gridwebdemo.war** на вашем веб-сервере. Пожалуйста, загрузите демонстрации с этой [ссылки](https://forum.aspose.com/uploads/discourse_instance3/22292).

Эта статья описывает, как запустить демонстрации Aspose.Cells для GridWeb на Java в сервере Apache Tomcat.

{{% /alert %}} 
### **Пошаговое руководство по запуску демонстраций GridWeb на Java**
1. Извлеките **apache-tomcat-7.0.52.zip** в любую директорию, например, C:\Tomcat 

![todo:image_alt_text](introduction-of-gridweb_1.png)



Следующий снимок экрана показывает извлеченные каталоги и файлы сервера Apache Tomcat 

![todo:image_alt_text](introduction-of-gridweb_2.png)



Возможно, вам также нужно установить переменную среды **CATALINA_HOME** 

![todo:image_alt_text](introduction-of-gridweb_3.png)

1. Откройте файл **tomcat-users.xml**. 

![todo:image_alt_text](introduction-of-gridweb_4.png)

1. Добавьте этого пользователя:

{{< highlight java >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**Здесь имя пользователя - tomcat, а пароль - secret** 

![todo:image_alt_text](introduction-of-gridweb_5.png)

1. Запустите файл **startup.bat**.
   Это запустит сервер Apache Tomcat. 

![todo:image_alt_text](introduction-of-gridweb_6.png)



**Сервер Tomcat запущен в командном окне** 

![todo:image_alt_text](introduction-of-gridweb_7.png)

1. Теперь откройте браузер и введите **localhost:8080**.
   Отобразится веб-страница Apache Tomcat. 

   **Веб-страница Apache Tomcat** 

![todo:image_alt_text](introduction-of-gridweb_8.png)

1. Нажмите **Manager App** и введите имя пользователя и пароль. (Как указано выше: tomcat, secret) 

![todo:image_alt_text](introduction-of-gridweb_9.png)

1. Прокрутите до раздела **WAR-файл для развертывания** и выберите файл **gridwebdemo.war**.
1. Нажмите **Развернуть**. 

![todo:image_alt_text](introduction-of-gridweb_10.png)

1. Выберите файл **gridwebdemo.war**. 

![todo:image_alt_text](introduction-of-gridweb_11.png)

1. Нажмите **Развернуть**. 

![todo:image_alt_text](introduction-of-gridweb_12.png)

1. Как только он будет развернут, нажмите **/gridwebdemo** и начните запускать демонстрации. 

![todo:image_alt_text](introduction-of-gridweb_13.png)


Отобразится страница демонстрации GridWeb. 

**Веб-страница демонстрации GridWeb** 

![todo:image_alt_text](introduction-of-gridweb_14.png)

1. Нажмите на любую демонстрацию и запустите ее. 

   **Запущена демонстрация создания контента** 

![todo:image_alt_text](introduction-of-gridweb_15.png)



**Запущена демонстрация таблиц** 

![todo:image_alt_text](introduction-of-gridweb_16.png)



**Заголовок панели и демонстрация кнопки команд** 

![todo:image_alt_text](introduction-of-gridweb_17.png)


## **Возможности браузеров и Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb - это веб-контроллер с графическим интерфейсом, который можно встраивать в веб-страницы JSP, подобно другим веб-контроллерам. Самое важное в веб-контроллере - это обеспечение поддержки различных браузеров. Aspose.Cells.GridWeb обеспечивает поддержку различных браузеров.
### **Сравнение**
Aspose.Cells.GridWeb полностью поддерживается в Microsoft Internet Explorer (IE). Однако в других браузерах у него есть небольшие ограничения. В этой теме представлено подробное сравнение поддержки различными браузерами различных функций.

|**Функции на стороне клиента**|**Microsoft Internet Explorer**|**Google Chrome**|**Mozilla Firefox**|**Opera**|
| :- | :- | :- | :- | :- |
|Контекстное меню ячейки|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|Проверка на стороне клиента|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Событие двойного щелчка|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Список ( *режим списка* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Список ( *режим всплывающего меню* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Ввод/редактирование формулы|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Закрепление или открепление строк/столбцов|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Гиперссылки ( *режим команды ячейки* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Гиперссылки ( *режим URL* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Объединение или разъединение ячеек|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Копирование/вставка нескольких ячеек|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Ввод/редактирование нескольких ячеек, один запрос|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Формат числа|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Разбиение по листам|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Только для чтения ячейки|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Только для чтения строк/столбцов|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Проверка данных с использованием регулярных выражений|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Изменить ширину столбца|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Изменить высоту строки|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Вставить/удалить строки и столбцы|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Прокрутить содержимое|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Прокрутить вкладки листа|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Установить границы ячеек|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Установить параметры шрифта ячеек|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}} Context menu of a cell can only be activated by clicking the Client side menu button.
