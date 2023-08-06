# Thirst App

Thirst App is an awesome application that from a few input parameters (drink type and amount of money) is capable to
order a drink, to quench your thirst, and show a cool message for the desired drink.

## How it works?

This app is based in two components:

* API

This API is the core of the app. It contains the business logic of the application and, giving some parameters,
returns the desired drink, or an error if something is wrong. Also, is in charge of storing the data to calculate
the benefits of the application.

* Web App

This is a simple page where the user enters the parameters (drink and money) and see what the
application returns. The page does not validate anything more than the input type, sending the data directly to the API
and showing the message to the user.

### Application business logic

So, this app is a common vending machine where the user will have to insert money and select the type of drink
they want, and it will return that beverage in case you insert the enough money and select an available drink
type. Easy peasy :)

| Parameter   | Type   | Required | Description                |
|-------------|--------|----------|----------------------------|
| drinkType   | string | true     | The drink ordered          |
| moneyAmount | float  | true     | Coins inserted by the user |

So, the application will have to accept any of those values and return some error messages once any of them are not
correct. The user should receive feedback about their action and see if the beverage is on hold, or the command was
failed.

### Extra point!

The owner of the business wants to know how much money she earns. So, the application should have a way to show how much
money do it earn with all the transactions. So, every time a user buy some product, the application will have to store
the amount to show it later.

### Tips

You would have to take some decisions during the Challenge, so here you could find some tips from our side:

* You would have to decide how the application looks like. Focus on UX and try to create a simple app, less is more.
  Avoid unnecessary buttons, give feedback to the user, etc...
* You have to decide what products should be available and how many items contains the application per each one. Try not
  to hardcode this but initialized with a migration, or a config file. Would be easy to maintain! :)
* As you would need to store the earnings, you would have to decide how to do so. The most important thing here is
  not to use one Database or another, but how decoupled is your code from the storage system. You can even use a
  JSON file to store this information 😉

## Technical requirements

* Create a **clean**, **maintainable** and **well-designed** code. We expect to see a good and clear architecture that
  allows to add or modify the solution without so much troubles.
* **Test** your code until you are comfortable with it. We don't expect a 100% of Code Coverage but some tests that
  help to have a more stable and confident base code.

To understand how you take decisions during the implementation, **please write a COMMENTS.md** file explaining some of
the most important parts of the application. You would also be able to defend your code through
[Rviewer](https://rviewer.io), once you submit your solution.

## How to submit your solution

* Push your code to the `devel` branch - we encourage you to commit regularly to show your thinking process was.
* **Create a new Pull Request** to `main` branch & **merge it**.

Once merged you **won't be able to change or add** anything to your solution, so double-check that everything is as you
expected!

Remember that **there is no countdown**, so take your time and implement a solution that you are proud!

<p align="center">
  If you have any feedback or problem, <a href="mailto:help@rviewer.io">let us know!</a> 🤘
  <br><br>
  Made with ❤️ by <a href="https://rviewer.io">Rviewer</a>
</p>
