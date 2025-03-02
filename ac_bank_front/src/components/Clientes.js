import React, { useEffect, useState } from "react";
import axios from "axios";

const Clientes = () => {
    const [clientes, setClientes] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/clientes/")
            .then((response) => setClientes(response.data))
            .catch((error) => console.error("Erro ao buscar clientes:", error));
    }, []);

    return (
        <div>
            <h2>Lista de Clientes</h2>
            <ul>
                {clientes.map((cliente) => (
                    <li key={cliente.id}>{cliente.nome} - {cliente.cpf}</li>
                ))}
            </ul>
        </div>
    );
};

export default Clientes;
