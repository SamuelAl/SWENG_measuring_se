import React from 'react'

export default function TextInput({params}) {
    const {label, type, id, name, placeholder, onChange, value} = params
    return (
        <div>
          <label htmlFor="email" className="block text-sm font-medium text-gray-700">
            {label}
          </label>
          <div className="mt-1">
            <input
              type={type}
              name={name}
              id={id}
              className="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md"
              placeholder={placeholder}
              onChange={onChange}
              value={value}
            />
          </div>
        </div>
      )
}
