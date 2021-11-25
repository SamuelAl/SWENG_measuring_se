import React from 'react'

export default function UserBadge({ user, onClick }) {
    console.log(user)
    return (
        <div className="flex gap-3 mb-4 bg-white rounded-md shadow hover:shadow-lg w-full h-20 overflow-hidden"
             onClick={() => onClick(user.name)}>
            <img src={user.avatar_url} alt="" />
            <div className="mt-4">
                <span className="text-lg text-gray-700">
                    {user.name}
                </span>
            </div>

        </div>
    )
}
