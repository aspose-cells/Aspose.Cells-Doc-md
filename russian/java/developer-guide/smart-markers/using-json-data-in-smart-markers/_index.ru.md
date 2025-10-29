---
title: Использование JSON данных в умных маркерах
type: docs
weight: 30
url: /ru/java/using-json-data-in-smart-markers/
---

## **Почему использовать JSON-данные в умных маркерах**
Почему использовать JSON-данные в качестве исходных данных для умных маркеров?
JSON (JavaScript Object Notation) — легкий читаемый человеком формат обмена данными, идеально подходит для структурирования иерархических данных. Вот почему он хорошо подходит в качестве исходных данных для умных маркеров (динамических заполнителей, которые автоматически заполняют таблицы, документы или панели управления):

1. Поддержка структурированных и иерархических данных
JSON изначально поддерживает вложенные объекты и массивы (например, { "user": { "name": "Alice", "orders": [ ... ] } }). Умные маркеры могут обходить эту иерархию (например, {{user.orders[0].price}}), что делает легким отображение сложных данных в шаблонах.

2. Независимость от языка и платформы
Парсеры JSON есть почти во всех языках программирования (Python, JavaScript, Java и др.). Инструменты, такие как Power Query в Excel, Google Apps Script или платформы без кода (например, Airtable), легко обрабатывают JSON.

3. Совместимость с API
Большинство современных API (например, REST, GraphQL) возвращают данные в формате JSON. Умные маркеры могут напрямую использовать живой JSON из веб-сервисов, обеспечивая обновление данных в реальном времени (например, цены акций, погода).

4. Читаемость и возможность отладки
Структура JSON в виде простого текста легко проверить (например, с помощью JSONLint). Можно редактировать вручную или через скрипты. Можно отлаживать при сопоставлении данных с маркерами.

5. Масштабируемость и гибкость
Добавлять/удалять поля в JSON без нарушения работы существующих умных маркеров (если опциональные поля обрабатываются аккуратно). Поддерживаются различные типы данных: строки, числа, логические значения, массивы и объекты.

6. Совместимость с экосистемами
Работает с современными инструментами обработки данных: базы данных: MongoDB, PostgreSQL (JSONB) и др. Инструменты для автоматизации: Zapier, Integromat. Конвейеры данных: Apache NiFi, Talend.

## **Использование вложенных шаблонов Excel с JSON-данными**
Aspose.Cells for Java поддерживает json-данные в умных маркерах, json-данные могут иметь иерархическую вложенность. Проверьте [шаблон](smartmarker.xlsx), [json-файл](smartmarker.json) и скриншот выходного файла excel, созданного с помощью следующего кода.

|**Первый лист файла smartmarker.xlsx с отображением умных маркеров.**|
| :- |
|![todo:image_alt_text](jsontemplate.png)|

|**Скриншот выходного файла Excel.**|
| :- |
|![todo:image_alt_text](jsonresult.png)|

Следующие данные JSON:
```json data
{
    "EntityCin" : "EntityCin Test",
    "EntityName" : "EntityName Test",
    "FirstName" : "FirstName Test",
    "MiddleName" : "MiddleName Test",
    "LastName" : "LastName Test",
    "DOB" : "2025-02-08",
    "SSN" : "11111111",
    "Directors" : [
        {
            "id" : "director id 1",
            "FirstName" : "director first 1",
            "MiddleName" : "director middle 1",
            "LastName" : "director last 1",
            "Reportees" : [
                {
                    "id" : "aaa",
                    "FirstName" : "first aaa",
                    "MiddleName" : "middle aaa",
                    "LastName" : "last aaa",
                    "Department" : "aaa department",
                    "City" : "aaa city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "bbb",
                    "FirstName" : "first bbb",
                    "MiddleName" : "middle bbb",
                    "LastName" : "last bbb",
                    "Department" : "bbb department",
                    "City" : "bbb city",
                    "GST" : "Yes",
                    "ITR" : "Yes"
                },
                {
                    "id" : "ccc",
                    "FirstName" : "first ccc",
                    "MiddleName" : "middle ccc",
                    "LastName" : "last ccc",
                    "Department" : "ccc department",
                    "City" : "ccc city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        },
        {
            "id" : "director id 2",
            "FirstName" : "director first 2",
            "MiddleName" : "director middle 2",
            "LastName" : "director last 2",
            "Reportees" : [
                {
                    "id" : "eee",
                    "FirstName" : "first eee",
                    "MiddleName" : "middle eee",
                    "LastName" : "last eee",
                    "Department" : "eee department",
                    "City" : "eee city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "fff",
                    "FirstName" : "first fff",
                    "MiddleName" : "middle fff",
                    "LastName" : "last fff",
                    "Department" : "fff department",
                    "City" : "fff city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        }
    ]
}
```
Приведенный ниже пример показывает, как это работает.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-Using-JSON-Data.java" >}}


## **Использование вложенного шаблона Excel с JSON-данными**
Aspose.Cells for Java поддерживает json-данные в умных маркерах, json-данные могут иметь иерархическую вложенность. В шаблоне использовалась функция подсчета итогов для статистики данных. Проверьте [шаблон](jsonExcelTemplate.xlsx), [json-файл](jsonData.json) и скриншот итогового файла Excel, созданного с помощью следующего кода.

|**Первый рабочий лист файла jsonExcelTemplate.xlsx с отображением смарт-маркеров.**|
| :- |
|![todo:image_alt_text](jsontemplate2.png)|

|**Скриншот выходного файла Excel.**|
| :- |
|![todo:image_alt_text](jsonresult2.png)|

Следующие данные JSON:
```json data
{
    "number": 10,
    "test": "test abc",
    "date": "2011-10-05T14:48:00.000Z",
    "arrayNumber": [1,2,3,4,5],
    "arrayWords": ["x1","xy2","yz3","z4"],
    "arrayOfObjects": [
      {"valNumber":12,"valString": "aa"},
      {"valNumber":15,"valString": "bb"},
      {"valNumber":1,"valString": "cc"},
      {"valNumber":20,"valString": "dd"}

    ],
    "nestedArray": [
      {"valNumber":12,"valString": "xy","nestArr": [{"val": 1,"some": "aa"}]},
      {"valNumber":15,"valString": "y","nestArr": [{"val": 2,"some": "bb"}]},
      {"valNumber":1,"valString": "yz","nestArr": [{"some": "cc"}]},
      {"valNumber":20,"valString": "z","nestArr": [{"some": "dd"}]}
    ],
  "Products": [
    { "ProductID": "A101", "ProductName": "Apples", "Units": 5 },
    { "ProductID": "A101", "ProductName": "Apples", "Units": 10 },
    { "ProductID": "B202", "ProductName": "Bananas", "Units": 7 },
    { "ProductID": "B202", "ProductName": "Bananas", "Units": 3 },
    { "ProductID": "C303", "ProductName": "Cherries", "Units": 8 }
  ]
}
```
Приведенный ниже пример показывает, как это работает.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-Using-JSON-Data-Subtotal.java" >}}

{{< app/cells/assistant language="java" >}}
