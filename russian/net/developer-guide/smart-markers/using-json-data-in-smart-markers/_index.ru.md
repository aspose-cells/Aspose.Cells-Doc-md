---
title: Умное импортирование JSON в Excel с помощью Smart Markers
type: docs
weight: 30
url: /ru/net/how-to-import-json-into-excel-with-smart-markers/
alias: [/net/using-json-data-in-smart-markers/]
---

## **Почему использовать JSON данные для Smart Markers**
Зачем использовать JSON данные в качестве исходных данных для Smart Markers?
JSON (JavaScript Object Notation) — это легкий, человекочитаемый формат обмена данными, идеально подходящий для структурирования иерархических данных. Вот почему он хорошо подходит в качестве исходных данных для Smart Markers (динамических заполнителей, автоматически заполняющих таблицы, документы или панели управления):

1. Поддержка структурированных и иерархических данных
JSON нативно поддерживает вложенные объекты и массивы (например, { "user": { "name": "Alice", "orders": [ ... ] } }). Smart Markers могут проходить по этой иерархии (например, {{user.orders[0].price}}), что облегчает сопоставление сложных данных с шаблонами.

2. Независимость от языка и платформы
JSON-парсеры существуют практически во всех языках программирования (Python, JavaScript, Java и др.). Инструменты, такие как Power Query в Excel, Google Apps Script или платформы без кода (например, Airtable), легко обрабатывают JSON.

3. Совместимость с API
Большинство современных API (например, REST, GraphQL) возвращают данные в формате JSON. Smart Markers могут напрямую использовать живой JSON из веб-сервисов, что позволяет обновлять данные в реальном времени (например, цены акций, погода).

4. Человекочитаемость и отладка
Структура JSON в виде текста легко проверить (например, с помощью JSONLint). Можно редактировать вручную или с помощью скриптов. Обеспечивает отладку при сопоставлении данных с маркерами.

5. Масштабируемость и гибкость
Добавление или удаление полей в JSON без нарушения работы существующих Smart Markers (если необязательные поля обрабатываются аккуратно). Поддержка различных типов данных: строки, числа, булевы значения, массивы и объекты.

6. Совместимость с экосистемой
Работает с современными инструментами обработки данных: базы данных: MongoDB, PostgreSQL (JSONB) и др. Инструменты автоматизации: Zapier, Integromat. Конвейеры данных: Apache NiFi, Talend.

## **Использование вложенного шаблона Excel с данными JSON**
Aspose.Cells for .NET поддерживает json данные в умных маркерах, json данные могут быть вложенными иерархически. Пожалуйста, ознакомьтесь с [шаблонным файлом](smartmarker.xlsx), [json файлом](smartmarker.json) и скриншотом выходного файла Excel, созданного с помощью следующего кода.

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

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-JSON-Data.cs" >}}


## **Использование шаблона Excel Subtotal с JSON данными**
Aspose.Cells for .NET поддерживает json данные в умных маркерах, json данные могут быть вложенными иерархически. В шаблоне Excel использовалась функция субтотал для статистики данных. Пожалуйста, ознакомьтесь с [шаблонным файлом](jsonExcelTemplate.xlsx), [json файлом](jsonData.json) и скриншотом выходного файла Excel, созданного с помощью следующего кода.

|**Первый рабочий лист файла jsonExcelTemplate.xlsx с отображением умных маркеров.**|
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

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-JSON-Data-Subtotal.cs" >}}

{{< app/cells/assistant language="csharp" >}}
