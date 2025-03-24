Feature: Логін на сайт

  Scenario: Успішний логін testtest
    Given користувач відкриває сторінку логіна
    When він вводить "user@example.com" і "password123"
    Then він бачить повідомлення "Вхід успішний"