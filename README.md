- [01. Introduction](#01-introduction)
  - [Source(s)](#sources)
- [02. User Flow](#02-user-flow)
  * [02.01. Public Routes](#0201-public-routes)
  * [02.02. Non-Elevated User Routes](#0202-non-elevated-user-routes)
  * [02.03. Elevated User Route](#0203-elevated-user-routes)
  * [02.04. Features Teased but **NOT** Implemented](#0204-features-teased-but-not-implemented)
- [03. Future Developments](#03-future-developments)


# 01. Introduction
The project, "PetSearch" is a concept Pet Adoption website that provides a front-end for:
- **Users** to both **search for pets** and contact pet rescue organizations about interest in pets for adoption, and
- **Pet Rescue Organizations**, private or public, to both **manage their database of pets with a GUI** and **allow users to search their listed pets**.

**PetSearch** is a full-stack application with the following features:
- Full-Stack application built using JavaScript, Flask, and PostgreSQL.
- Features public, user, and restricted elevated (Pet Rescue Organization and Admins) routes.
- Features API endpoints for returning JSON.

The motivation for **PetSearch** is to:
1) ~6.3 mn companion animals ("pets", dogs and cats) entered a pet shelter as of 2019<sup>[1]</sup> and at any given time, there are an estimated 70 mn strays roaming on US streets alone<sup>[2]</sup>. 920,000 were euthanized in 2019 alone<sup>[1]</sup>.
2) There are a total of ~3,500 municipal shelters and ~10,500 "animal rescue organizations", consisting mostly of privately- and mixed-funded pet shelters, in the United States<sup>[2]</sup>. In total, it is claimed that U.S. taxpayers directly fund animal shelters ~$1-2 bn/yr (0.03% USA FY2020 Budget, 0.01% USA 2020 GDP)<sup>[2]</sup>.
3) Most of these shelters<sup>[3]</sup>, even if they have an Excel Spreadsheet equivalent or better ("database system"), unlikely has a robust database search system for users to search their database to find a pet within their search parameters. **PetSearch** fulfills that demand so that:
    - **Animal rescue organizaions** may focus on taking care of pets searching for a home and improving adoption rates. Because animal rescue organizations won't have to spend resources to find and/or keep a technical individual, say a software engineer, to setup and/or manage their database that makes it easier for
    - **Users** to easily search for pets listed for adoption.

## Source(s)
[1] Unknown. *Pet Statistics*. **American Society for the Prevention of Cruelty to Animals**. https://www.aspca.org/helping-people-pets/shelter-intake-and-surrender/pet-statistics (retrieved 2022-08-30)

[2] Cvetkovska, L. *44 Shocking Animal Shelter Statistics (2022 Update)*. **petpedia.co**. https://petpedia.co/animal-shelter-statistics/#14,000%20shelters%20and%20rescue%20groups (updated 2022-02-18, retrieved 2022-08-30)

[3] **Dude trust me**.

# 02. User Flow
## 02.01. Public Routes
- Login, Register, Request Rescue Organization Account
[![02.01.a](https://github.com/YiJohnZhang/sb_Capstone_Project_01/blob/main/README_assets/02.01.a_2022-09-01_21-42-42.png)](https://user-images.githubusercontent.com/8562595/188060462-99c591f3-ffa6-44d3-8b94-a3bb367493e6.mp4)
- Search Pets
[![02.01.b1](https://github.com/YiJohnZhang/sb_Capstone_Project_01/blob/main/README_assets/02.01.b1_2022-09-01_21-43-54.png)](https://user-images.githubusercontent.com/8562595/188060457-eabb5a87-5ba4-41c2-9b2c-0246960ec150.mp4)
[![02.01.b2](https://github.com/YiJohnZhang/sb_Capstone_Project_01/blob/main/README_assets/02.01.b2_2022-09-01_21-44-27.png)](https://user-images.githubusercontent.com/8562595/188060441-49997a46-1ac0-4420-9bc0-5fbd990b5eba.mp4)
- View Pets
[![02.01.c](https://github.com/YiJohnZhang/sb_Capstone_Project_01/blob/main/README_assets/02.01.c_2022-09-01_21-45-01.png)](https://user-images.githubusercontent.com/8562595/188060437-2a50f7c2-3f9c-49ec-ad68-828747a0cda2.mp4)

## 02.02. Non-Elevated User Routes
All of **Public Routes** and additional tasks:
- Edit User Profile
[![02.02.1](https://github.com/YiJohnZhang/sb_Capstone_Project_01/blob/main/README_assets/02.02.1_2022-09-01_21-45-24.png)](https://user-images.githubusercontent.com/8562595/188060328-7eec77a1-0230-4446-96a2-d31770fb3ecf.mp4)
[![02.02.2](**IMAGELINK**)]()
- *Not Implemented*: Send Messages to other Users and Favorite Pets

## 02.03. Elevated User Routes
All of **(Non-Elevated) User Routes** and a Database Management System, depending on the elevated user type:
- Pet Rescue Organizations ("rescueAgency") can only manage pets they have listed (edit and delete) or add new pets to the database.
[![02.03.a](https://github.com/YiJohnZhang/sb_Capstone_Project_01/blob/main/README_assets/02.03.a_2022-09-01_21-45-56.png)](https://user-images.githubusercontent.com/8562595/188060167-b8e3c137-00e1-46a2-9f96-a27963994d14.mp4)
- Administrators ("admin") can remove any pet(s) from the database and remove any non-admin user(s) from the database.
[![02.03.b](https://github.com/YiJohnZhang/sb_Capstone_Project_01/blob/main/README_assets/02.03.b_2022-09-01_21-29-22.png)](https://user-images.githubusercontent.com/8562595/188058719-9470f865-cfaa-4653-932b-152dde950e60.mp4)


## 02.04. Features Teased but **NOT** Implemented
- General
    - Request Rescue Organization Account (i.e. sends a message to an administrator for approval and manual creation of a database account)
	- Toggle Favorite (pet)
	- See Favorite pets
	- Message (user/about pet)
	- Report (pet)
- Elevated User Commands (Rescue Agency)
	- Import Database as CSV
	- Export Database as CSV
	- Toggle "Pet Adopted"
- Elevated User Commands (Admin)
	- Ban (user)

# 03. Future Developments
**Date Completed**: R, 2022-09-01. Just 1 day and no cake :(

If I had more time beyond the 2 weeks to both work on and document this project, I would have:
- Database Redesign: A design decision that I made early on in the schema design to reduce space-complexity that introduces one inconvenience to maintain the code base (`app.py: petView: line 420 to 425`).
- UI: Made the Elevated User UI more pretty. Ad tooltips to the UI.
- User signup has email verification for non-elevated users and location verification (for rescue organization).
- Change user password.
- Search categories: search by rescue organization and more pet search parameters.
- User interaction, such as `Direct Messagse`, and `Favorites`.
- Administrator QOL improvements, a search feature in the administrator panel:
    - Rescue Organizations
	    - Query and sort their pet listings by pet name, gender, pet specie, pet breed, coat hair type, coat pattern, primary light shade, primary dark shade.
    - Administrators
	    - Query and sort users by rescue organization, `LIKE`sql username, `LIKE`sql last name/first name, account status (not a database attribute, i.e. banned or active), complaints (not a database attribute)
- API key and API routes to support widgets for rescue organizations to display a search method on their website.
