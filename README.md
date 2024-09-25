# **Fufu Republic Restaurants Data Generation & Transformation.**

## **Introduction.**

Previously, I designed the [Fufu Republic Restaurants Data Model ](https://github.com/Samuel-Njoroge/fufu-republic-data-modeling) .

This project entails an implementation of the model, data transformation and storage.

## **Architecture.**
![arh](https://github.com/Samuel-Njoroge/fufu-republic-data-transformation/blob/main/diagrams/data%20transformation.svg)

The process includes:

1. Generating fake data using the Faker library.
2. Loading the generated data as seed files in dbt (data build tool).
3. Transferring the data to Snowflake.
4. Performing transformations on the data.
5. Loading the transformed data back into Snowflake.

## Technologies

- *Python*: For data generation scripts.
- *Faker*: Library for generating synthetic data.
- *dbt (data build tool)*: For data transformation and modeling.
- *Snowflake*: Cloud data warehouse.

## Skills Learned

1. Data generation techniques using Python and Faker
2. ETL (Extract, Transform, Load) processes
3. Data modeling and transformation using dbt
4. Working with cloud data warehouses (Snowflake)

## Set Up Guide.

1. **Clone the repository**
   ```
   git clone https://github.com/Samuel-Njoroge/fufu-republic-data-transformation
   
   cd fufu-republic-data-transformation
   ```

2. **Set up a Python virtual environment**
   ```
   python -m venv venv
   
   source venv/bin/activate
   ```

3. **Install required Python packages**
   ```
   pip install -r requirements.txt
   ```

4. **Generate synthetic data**
   ```
   python generate_data.py
   ```

5. **Set up dbt**
   
   Navigate to the dbt directory
     
   ```
   cd fufu_dbt
   ```
   
   Configure your `profiles.yml` file with your Snowflake credentials.

7. **Load seed data and run dbt models**
   ```
   dbt seed
   
   dbt run
   ```
   An example of the output.

   ![seed](https://github.com/Samuel-Njoroge/fufu-republic-data-transformation/blob/main/diagrams/seed-complete.png)

8. **Verify data in Snowflake**
   - Log in to your Snowflake account.
   - Query the transformed tables to confirm the data pipeline's success.

     An example of the output.

    ![data](https://github.com/Samuel-Njoroge/fufu-republic-data-transformation/blob/main/diagrams/views.png)

## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request with your proposed changes.
